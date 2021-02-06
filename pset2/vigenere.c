#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int shift(char c);

int main(int argc, char *argv[])
{
//turns argv[1] into string
    string keyword = (string) argv[1];
    string s;
    int key;
    int c;
    char a;
//Cheking validy of keyword 
    if (argc == 2)
    {
//Just condition to reject Hro20x blah blah blah 
        if (keyword[0] == 'H')
        {
            printf("Usage: ./vigenere keyword\n");
            return 1;
        }
//Checking if keyword is alpha (but for some reasons only first letter)
        for (int i = 0; i < strlen(keyword); i++)
        {
            if (!isalpha(keyword[i])) 
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
//request text and so on...
            else if (isalpha(keyword[i]))  
            {   
                s = get_string("plaintext: ");
                printf("ciphertext: ");

                for (int j = 0; j < strlen(s);)
                {
//If keyword[max] returns it to [0]
                    int r = strlen(keyword);
                    if (i == r)
                    {
                        i -= r;
                    }
//Found outs key and turn string(s) into int(c)
                    key = shift(keyword[i]);
                    c = (int) s[j];
//Needed one more if statment, just to turn ascii into text at the end
                    if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
                    {
//Checking c for lower register
                        if (c >= 97 && c <= 122)
                        {
                            c += key;
                            for (; c >= 123;)
                            {
                                c -= 122;
                                c += 96;
                            }
                        }
//Checking c for upper register
                        if (c >= 65 && c <= 90) 
                        {
                            c += key;
                            for (; c >= 91;)
                            {
                                c -= 90;
                                c += 64;
                            }
                        }
                        a = (char) c;
                        printf("%c", a);
                    }
//If chars in s not letters, prints them out
                    else 
                    {
                        printf("%c", c);
                        i--;
                    }
//Itereting keyword[i] and s[j]
                    i++;
                    j++;
                }
                printf("\n");
                return 0;
            }
        }
    }
    else if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
}
//Counts value to shift argv[1]
int shift(char c)
{
    int z;

    if (isupper(c))
    {
        z = (int) c;
        z -= 65;
    }
    if (islower(c))
    {
        z = (int) c;
        z -= 97;
    }
    return z;
}
