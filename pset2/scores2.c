#include <stdio.h>
#include <cs50.h>
//Global varianle (DO NOT CHANGE!!!)
const int COUNT = 3;

void chart (int scores);

int main (void)
{
    //Get scores from user
    int scores[COUNT];
    for (int i = 0; i < COUNT; i++)
    {
        scores[i] = get_int ("Score %i: ", i + 1);
    }
    //Chart scores
    for (int i = 0; i < COUNT; i++)
    {
        printf ("Score %i: ", i + 1);
        chart(scores[i]);
    }
}

void chart (int scores)
{
    for (int i = 0; i < scores; i++)
    {
        printf ("#");
    }
    printf ("\n");
}
