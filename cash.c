#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)

//greedy algorithm. dispense change in fewest number of coins.

{

    float n;
    int m;

    do
    {
        n = get_float("Change owed: ");
    }

    while (n < 0);

    n = round(n * 100);

    m = (int)n;


    int j = 0;

    while (m >= 25)
    {
        (m = (m - 25), j++);
    }

    while (m >= 10 && m < 25)
    {
        (m = (m - 10), j++);
    }

    while (m >= 5 && m < 10)
    {
        (m = (m - 5), j++);
    }

    while (m >= 1 && m < 5)
    {
        (m = (m - 1), j++);
    }


    printf("%i\n", j);

}
