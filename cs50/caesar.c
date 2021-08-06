#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, string argv[]) {
    // Check for only 2 arguments
    if (argc != 2) {
        printf("Usage: ./caesar key\n");
        return 1;
    }



    // Check that all key is a digit
    string key = argv[1];

    for(int i = 0;i < strlen(key); i++ ) {
        int char_int = (int) key[i];
        if (char_int > 57 || char_int < 48) {
              printf("Usage: ./caesar key\n");
              return 1;
        }
    }

    int key_num = atoi(key);

    // prompt for plaintext
    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;

    for(int j = 0; j < strlen(plaintext); j++) {
        if (isalpha(plaintext[j])){
            //if char is Uppercase
            if (isupper(plaintext[j])){
                ciphertext[j] = ((((int)plaintext[j]-65) + key_num)%26)+65;
            }
            //if char is lowercase
            else {
                ciphertext[j] = ((((int)plaintext[j]-97) + key_num)%26)+97;
            }
        }
        //if char is not alphabetical
        else {
            ciphertext[j] = plaintext[j];

        }

    }
    //Return Answer Ciphertext
    printf("ciphertext: %s\n", ciphertext);

}
