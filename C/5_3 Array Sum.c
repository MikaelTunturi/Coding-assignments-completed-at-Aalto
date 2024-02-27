#include "source.h"
#include <stdio.h>

/**
 * \brief Calculates the sum of integer elements in an array
 *
 * \param array An array of integers
 * \param count The number elements in the array
 * \return The sum of the elements
 */
int array_sum(int *array, int count)
{
    int sum = 0;
	for (int a = 0; a < count; a++) {
		sum += array[a];
	}
	return sum;
}