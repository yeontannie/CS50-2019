import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks""" #TODO

    id = int(session['user_id'])
    info = db.execute("SELECT name, token, shares FROM  portfolio WHERE id=:id ORDER BY token ", id=id)
    cash = db.execute("SELECT cash FROM users WHERE id=:id", id=id)
    CASH = cash[0]["cash"]

    stocks = []

    for i in info:
        token = lookup(i["token"])
        shares = i["shares"]

        temp = {
            "symbol": token["symbol"],
            "shares": shares,
            "name": token["name"],
            "price": token["price"],
            "total": token["price"] * shares
        }

        stocks.append(temp)

    ttotal = (CASH + sum([stock["total"] for stock in stocks]))

    db.execute(f"DELETE FROM portfolio WHERE shares={0}")

    return render_template("index.html", CASH=CASH, stocks=stocks, ttotal=ttotal)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock""" #TODO

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        token = lookup(request.form.get("symbol"))
        price = usd(token["price"])
        value = token["price"] * int(shares)
        id = int(session['user_id'])
        name = token["name"]

        if not symbol or not shares:
            return apology("must enter symbol and shares quontity", 400)

        if shares <= 0:
            return apology("provide positive integer", 400)

        if token == None:
            return apology("symbol is not valid", 400)

        cash = db.execute("SELECT cash FROM users WHERE id=:id", id=id)

        if int(cash[0]["cash"]) < value:
            return apology("you have not enough money", 400)

        else:
            stock = db.execute("SELECT * FROM portfolio WHERE token=:symbol AND id = :id", symbol=symbol, id=id)

            if len(stock) == 0:
                db.execute("INSERT INTO portfolio (id, name, token, price, shares) VALUES (:id, :name, :token, :price, :shares)",
                        id=id, name=name, token=symbol, price=token["price"], shares=shares)

            else:
                sowned = db.execute("SELECT shares FROM portfolio WHERE token = :token", token=symbol)
                cshares = sowned[0]['shares']
                update = cshares + shares
                db.execute("UPDATE portfolio SET shares=:update WHERE id=:id AND token = :token", update=update, id=id, token=symbol)

            db.execute("INSERT INTO history (id, token, shares, price) VALUES (:id, :token, :shares, :price)", id=id,
                        token=symbol, shares=shares, price=token["price"])

            db.execute("UPDATE users SET cash = cash - :value WHERE id = :id", value=value, id=id)

        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format""" #TODO

    username = request.args.get("username")

    if len(username) == 0:
        return jsonify(False)

    check = db.execute("SELECT username FROM users WHERE username=:un", un=username)

    if len(check) == 0:
        return jsonify(True)
    else:
        return jsonify(False)

@app.route("/history")
@login_required
def history():
    """Show history of transactions""" #TODO

    id = int(session['user_id'])
    info = db.execute("SELECT * FROM  history WHERE id=:id", id=id)

    stocks = []

    for i in info:
        token = lookup(i["token"])
        shares = i["shares"]
        transaction = i["transaction"]

        temp = {
            "symbol": token["symbol"],
            "shares": shares,
            "price": token["price"],
            "transaction": transaction
        }

        stocks.append(temp)

    return render_template("history.html", stocks=stocks)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote.""" #TODO

    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("must enter symbol", 400)

        if request.form.get("symbol"):
            quote = lookup(request.form.get("symbol"))

            if quote == None:
                return apology("Symbol is not valid", 400)

            else:
                return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=usd(quote["price"]))

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user""" #TODO
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password", 403)

        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("confirmation and password must be the same", 403)

        #hash password
        phash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=2)

        # Query database for username
        rows = db.execute("INSERT INTO users (username, hash) VALUES (:username, :phash)", username=request.form.get("username"), phash=phash)

        if not rows:
            return apology("username already taken")

        session["user_id"] = rows

        return redirect("/")

    else:
       return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock""" #TODO

    if request.method == "POST":

        #things want to sell
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        id = int(session['user_id'])
        curprice = lookup(symbol)["price"]

        curshares = db.execute("SELECT shares FROM portfolio WHERE token=:symbol AND id=:id", symbol=symbol, id=id)[0]["shares"]
        curcash = db.execute("SELECT cash FROM users WHERE id=:id", id=id)[0]["cash"]

        if not symbol or not shares:
            return apology("must enter symbol and shares", 400)

        if shares <= 0:
            return apology("shares is not valid", 400)

        if curshares < shares:
            return apology("you don't have that many stock")

        zero = db.execute(f"UPDATE portfolio SET shares = {curshares - shares} WHERE id=:id AND token = :symbol ", id=id, symbol=symbol)
        db.execute(f"UPDATE users SET cash = {curcash + (curprice * shares)} WHERE id=:id", id=id)
        db.execute("INSERT INTO history (id, token, shares, price) VALUES (:id, :token, :shares, :price)", id=id,
                            token=symbol, shares="-" + str(shares), price=curprice)

        if zero == 0:
            db.execute(f"DELETE FROM portfolio WHERE shares=={0}")

        flash("Sold!")
        return redirect("/")

    else:
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
