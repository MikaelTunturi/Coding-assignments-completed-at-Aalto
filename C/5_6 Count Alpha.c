#include "source.h"

#include <stdio.h>
#include <ctype.h>
#include <string.h>

/**
 * \brief Counts alphabetical characters in a string
 *
 * \param str The string to be processed
 * \return The number of alphabetical characters
 */

//for (int a = 0; a < sizeof(str); a++) {

int count_isalpha(const char *str)
{
    int number = 0;
	while (*str != '\0') { //str päättyy merkkiin '\0'
		if (isalpha(*str)) {
			number++;
		}
		str++;
	}
	return number;
}
