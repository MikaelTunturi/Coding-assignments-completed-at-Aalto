#include "source.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

/* Print string */
/* Parameters:
 * s: string to be printed */

/**
 * \brief Prints ? terminated string
 *
 * \param s A ? terminated string
 */
void qstr_print(const char *s)
{
    while (*s != '?') {
		printf("%c", *s);
		s++;
	}
}

/**
 * \brief Returns the length of a ? terminated string
 *
 * \param s A ? terminated string
 * \return The number of characters before first occurrence of ?
 */
unsigned int qstr_length(const char *s)
{
    unsigned int number = 0;
	while (*s != '?') {
		number++;
		s++;
	}
	return number;
}

/**
 * \brief Concatenates two ? terminated strings
 *
 * \param dst The ? terminated string that will contain the concatenated ? terminated string
 * \param src A ? terminated string that will be appended to dst.
 * \return The length of the dst after concatenation
 */
int qstr_cat(char *dst, const char *src)
{
    int a = 0;
	int b = qstr_length(dst);
	while (src[a] != '?') {
		dst[b] = src[a];
		a++;
		b++;
	}
	dst[b] = '?';
	int number = qstr_length(dst);
	return number;
}
