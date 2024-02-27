#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/**
 * \brief Compares two integers and returns their comparison result.
 * \details This function defines the order of the elements by 
 *          returning (in a stable and transitive manner): 
 *          <0	The value pointed to by 'a' goes before the value pointed to by 'b'
 *           0	The value pointed to by 'a' is equivalent to the value pointed to by 'b'
 *          >0	The value pointed to by 'a' goes after the value pointed to by 'b'
 * 
 *          In other words, this function essentially calculates the difference
 *          of the values pointed by its arguments.
 * 
 * \param a A pointer to the integer that will be compared against the 
 *          value pointed by b.
 * \param b A pointer to the integer that will be compared against the 
 *          value pointed by a.
 * \return The comparison result
 */
int compare_ints(const void* a, const void* b) {
	return *(int*) a - *(int*) b;
}

/**
 * \brief Finds the difference between median and mean value of the 
 * elements in an integer array.
 * 
 * \details This function calculates the mean and finds the median value
 * 			of the array numbers, which contans n number of elements.
 * 			It assumes that n is an odd integer when finding the median value.
 * 			The mean value is calculated using integer division on sum of 
 * 			the all elements in the array.
 * 
 * \param numbers Array of the numbers, which contains n integer elements 
 * \param n The number of elements in the array. It is always an odd 
 * integer greater than 1.
 * 
 * \return the difference between median and mean of the array. 
 * 
 * \note Median is the middle element of the array when it is sorted.
 *       
 *       stdlib.h has some useful functions that might help you to
 *       sort the array to find the median value. You might need 
 *       the comparison function compare_ints if you prefer to 
 *       use stdlib function for sorting the array.
 * 
 * \note The mean value is the arithmetic average of the values in the array.
 *      
 *       When calculating the mean value, you should use integer arithmetic 
 *       to find the average. If you use floating point arithmetic, you might 
 *       get a wrong result. 
 * 
 * \note In your implementation, do not write to stdout to check the functionality.
 *       You should use my_tests function to print and check the functionality 
 *       of your implementation.
 */
int diff_median_mean(unsigned int* numbers, unsigned int n) {
	int mean = 0, median = 0;
	//TODO: implement your function here!
	// Let's calculate the mean at first.
	int total = 0;
	for (unsigned int i = 0; i < n; i++) {
		total += numbers[i];
	}
	mean = total/n;
	// Let's calculate the median then.
	qsort(numbers, n, sizeof(int), compare_ints);
	median = numbers[n/2];
	return median - mean;
}

/**
 * \brief conducts the tests for your implementation.
 * 
 * \details You are strongly encouraged to test your implementation
 * using this function. Try to create at least three test cases to check
 * whether your function implementation is correct.
 * 
 */
void my_tests(void) {
	// You can write your own test code here.
}
int main(void) {
	/* You may implement your own tests in my_tests function */
	my_tests();
	return 0;
}