#include<stdio.h>
#include<cs50.h>

bool valid_triangle(float a, float b, float c);

int main(void)
{
    float a = get_float ("Give me an a: ");
    float b = get_float ("Give me a b: ");
    float c = get_float ("Give me a c: ");

    valid_triangle(a, b, c);
}

bool valid_triangle(float a, float b, float c)
{
    if (a <= 0 || b <= 0 || c <= 0)
    {
        return false;
    }
    else if (a + b <= c || b + c <= a || a + c <= b)
    {
        return false;
    }
    return true;
}
