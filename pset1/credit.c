#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
    int counter = 0;
    long num;
    int tsum;
    int sumt = 0;
    int sum;
    long sec;
    long thi;
    long fi;
    long fo;
    long first;
//Get Credit Card Number from user
    do
    {
        num = get_long("Number: ");
    }
    while (num < 1);
//Indicates first number of credit card
    first = num;
    while (first >= 100)
    {
        first /= 10;
    }
//Lun's Algoritm
    for (sec = num; sec > 10; sec /= 100)
    {
        thi = ((sec % 100) / 10) * 2;

        if (thi <= 9)
        {
            tsum = thi + tsum;
        }
        if (thi >= 10)
        {
            int n = thi;
            int dec = thi;
            dec %= 10;
            n /= 10;
            tsum = dec + n + tsum;
        }
    }
    for (fo = num; fo > 1; fo /= 100)
    {
        fi = fo % 10;
        sumt = fi + sumt;
    }
    sum = tsum + sumt;
//Indicates Credit Card
    if (sum % 10 == 0)
    {
        //Can count numbers
        //string s = get_string ("Number: ");
        //int n = strlen(s);
        //printf("Counter: %i\n", n);
// Indicates couter
        while (num > 0)
        {
            num /= 10;
            counter++;
        }
        if ((counter == 15) && (first == 34 || first == 37))
        {
            printf("AMEX\n");
        }
        if ((counter == 16) && (first == 51 || first == 52 || first == 53 || first == 54 || first == 55))
        {
            printf("MASTERCARD\n");
        }
        if ((counter == 13 || counter == 14 || counter == 15 || counter == 16) && (first >= 40 && first <= 49))
        {
            printf("VISA\n");
        }
        else if (counter <= 12)
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
