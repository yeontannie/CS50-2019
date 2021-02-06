#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h<=0 || h>8);
    for (int l=0; l<h; l++)
    {    
        for( int s=h-l; s>1; s--)
        {
            printf(" ");
        }
        for (int v=0; v<l+1; v++)
        {
            printf("#");
        }
        {
            printf("  ");
        }
      for (int v=0; v<l+1; v++)
        {
            printf("#");
        }
        printf("\n");
    }
}  
