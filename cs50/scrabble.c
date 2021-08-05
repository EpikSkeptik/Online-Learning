#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2) {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2) {
        printf("Player 2 wins!\n");
    }
    else {
        printf("Tie!\n");
    }


}

int compute_score(string word)
{
    // Declare count and set to 0
    int count = 0;

    // Check through all the characters in word
    for (int i = 0; i < strlen(word); i++) {
        char c = word[i];
        int c_int = (int) c; //Get the ASCII digit of character

        // Check for uppercase
        if (isupper(c)) {
            // A starts at 65 but is index 0 of our POINTS[]
            count += POINTS[c_int-65];
        }
        // Check for lowercase
        else if (islower(c)) {
            // a starts at 97 but is index 0 of our POINTS[]
            count += POINTS[c_int-97];
        }

    }
    return count;
}