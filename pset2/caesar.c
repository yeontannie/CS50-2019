#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char *argv[])
{
    int key;
    int c;
    char a;
//Checking validy of key
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (argc == 2)
    {
        key = atoi(argv[1]);
//If in argv[] text or smth, doing this
        if (key == 0)
        {
            printf("Usage: ./caesar key\n");
        }
//Checking once more, if ok, request a text
        if (key >= 1 || key <= 9)
        {
            string s = get_string("plaintext: ");
            printf("ciphertext: ");
//Printing out text and its ascii
            for (int i = 0; i < strlen(s); i++)
            {
                c = (int) s[i];
                if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
                {
                    c += key;
                    for (; c >= 123;)
                    {
                        c -= 122;
                        c += 96;
                    }
                    a = (char) c;
                    printf("%c", a);
                }
                else 
                {
                    printf("%c", c);
                }
            }
            printf("\n");
        }
         return 0;
    }
    else 
    {
        printf("Usage: ./caesar key\n"); 
    }
}
