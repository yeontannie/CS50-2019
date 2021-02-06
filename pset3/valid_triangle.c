#include <stdio.h>
#include <cs50.h>

const int SIDES = 3;

int main(void)
{
    int side[SIDES];
//Get integer from user
    for(int i = 0; i < SIDES; i++)
    {
        side[i] = get_int ("Give me a number %i: ", i + 1);
    }
//Check if sides is correct
    if((side <= 0) || (side[0] + side[1] < side[2]) || (side[1] + side[2] < side[0]) || (side[0] + side[2] < side[1]))
    {
        printf("false\n");
    }
    else
    {
        printf ("true\n");
    }
}


