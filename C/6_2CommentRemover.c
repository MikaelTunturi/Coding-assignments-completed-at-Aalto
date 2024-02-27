#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "source.h"

/**
 * \brief Removes the C comments from the input C code.
 *
 * \details The function polishes the code by */
//          - removing the block comments delimited by /* and */.
/*            These comments may span multiple lines.You should remove only */
//            characters starting with /* and ending with */. The characters,
/*            including white space characters (' ', \n, \r, \t), */
//            after */ should not be removed.
/*
 *          - remove the line comments starting with // until and including the
 *            newline character \n.
 *
 * \param input A code segment that contains some comments.It is a dynamically
 *              allocated string(array of characters).
 * \return A pointer to the polished code
 */

char *delete_comments(char *input)
{
    int size = strlen(input)+1; // +1, jotta viimeinen merkki '\0' sisältyy
	char *cleared_input = malloc(size * sizeof(char));
	char *original_copy = input;
	int i = 0;
	
	while (*input != '\0') {
		if (*input == '/' && *(input+1) == '/') {
			//input++; // tämä ei taida olla tarpeellinen
			while (*input != '\n') {
				input++; // perustuuko siihen, että siirretään eteenpäin
						 // ja tallennetaan toiseen jonoon vain halutut?
			}
			input++; // poistetaan vielä rivinvaihtomerkki!
		}
		else if (*input == '/' && *(input+1) == '*') { // VIRHE OLI ILMEISESTI TÄSSÄ LOHKOSSA AIEMMIN.
            input++;
            input++;
            //while ((*input != '*' && *(input+1) != '/') || (*input == '*' && *(input+1) != '/') || (*input != '*' && *(input+1) == '/')) {
            while ((*input != '*' && *(input+1) != '/') || (*input != '*' && *(input+1) == '/') || (*input == '*' && *(input+1) != '/')) {
			// TÄRKEÄ HUOMIO: käydään kaikki kolme tapausta läpi yllä olevassa while-loopissa.	
				input++;
            }
            input++;
            input++;
        }
		else {
			cleared_input[i] = *input;
			i++;
			input++;
		}
	}
	cleared_input[i] = '\0'; // viimeisessä else-kohdassa lisätään i:n arvoa
							 // 1:llä, joten siinä indeksissä *input == '\0'
							 // ja sen takia while-loop loppuu. Lisätään
							 // siis merkki '\0' myös puhdistettuun jonoon.
	free(original_copy);
	return cleared_input;
}
