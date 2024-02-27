#include <stdio.h>

/**
 * \brief Counts the number of occurrences of characters in an array
 *
 * \param array A zero (0) terminated string that is composed some number of characters
 * \param counts An int array of 256 elements that contains number of character occurrences.
 */

void countchars(/*const char*/ unsigned char *array, unsigned int *counts) // muutos tässä
{
	if (array != NULL) {
		for (int a = 0; array[a] != 0; a++) {
		counts[array[a]]++; //jos array[a] == 3 niin counts[3]++;
		}
	}
}
