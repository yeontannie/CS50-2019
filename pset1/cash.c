#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(void)
{
    float dollars;
    int count = 0;
    do
    {
        dollars = get_float("Change Owed: ");
    }
    while(dollars <= 0);

    int coins = round(dollars*100);

    while(coins >= 25)
    {
        coins-=25;
        count ++;
    }
    while(coins >= 10)
    {
        coins-=10;
        count ++;
    }
    while(coins >= 5)
    {
        coins%=5;
        count ++;
    }
    while(coins >= 1)
    {
        coins%=1;
        count ++;
    }
    printf("I owe you %i\n", count);
}
