#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height<=0 || height>8);

    for (int l = 0; l < height; l++)
    {
        for (int s = height-l; s > 1; s--)
        {
            printf(" ");
        }
        for (int hash = 0; hash < l+1; hash++)
        {
            printf("#");
        }
        printf ("\n");
    }
}
