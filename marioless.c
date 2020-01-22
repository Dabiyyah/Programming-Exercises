#include <stdio.h>
#include <cs50.h>

int main(void)

{
   int m, n;


   do
    {
        n = get_int("Give me A Positive Number Between 0 and 23, inclusive: ");
    }

    while (n < 0 || n > 23);

    m = (n-1);

    for (int i=0; i <= (n-1); i++)
    {

        for (int j = 0; j <= (m-1); j++)
        {
            printf(" ");
        }

        m--;

        for (int k = 0; k <= (i+1); k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
