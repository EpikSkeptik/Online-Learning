#include <stdio.h>
#include <cs50.h>
#include <math.h>

//Calculate yearly population
int year_pop(start_pop){
    int born = floor(start_pop/3);
    int dead = floor(start_pop/4);

    return start_pop + born - dead;
}

int main(void) {
    //Initialize Start/End Populations
    int start_pop, end_pop, years = 0;

    //Get Start Size for population
    do {
        start_pop = get_int("Start Size: ");
    }
    while (start_pop < 9);

    //Get End Size for population
    do {
        end_pop = get_int("End Size: ");
    }
    while (end_pop < start_pop);

    //Check if no years
    if (start_pop == end_pop) {
       printf("Years: %i", 0);
    }
    //Calculate number of years
    else {
        do {
            start_pop = year_pop(start_pop);
            years += 1;
        } while (start_pop < end_pop);

        printf("Years: %i \n", years);
    }

}