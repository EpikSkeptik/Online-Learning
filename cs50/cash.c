#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void) {
    int coins = 0;
    float change_dollars = 0;
    // Prompt get float change
    do {
        change_dollars = get_float("Changed owed: ");
    } while (change_dollars <= 0 );

    // Change to cents
    int cents = round(change_dollars*100);

    // Coun coins
    coins += floor(cents / 25);
    cents = cents%25;
    coins += floor(cents/10);
    cents = cents%10;
    coins += floor(cents/5);
    cents = cents%5;
    coins += cents;

    printf("%i\n", coins);


}