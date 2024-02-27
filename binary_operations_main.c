#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/**
 * \brief Counts the number of set bits in a byte array of n elements.
 * 
 * \details This function counts the number set bits in a byte array. 
 *          For example, if array = {0xA3, 0x58} and n = 2, the array 
 *          bytes has binary values 1010 0011 0101 1000, and the function
 *          returns 7. Since 
 *          1010 0011 0101 1000
 *          ^ ^    ^^  ^ ^ ^   
 *          has 7 set bits.
 * 
 * \param array A byte array of n elements.
 * \param n The number of bytes in array.
 * \return The number of set bits in the bytes of array.
 * 
 * \note In your implementation, do not write to stdout to check the functionality.
 *       You should use my_tests function to print and check the functionality 
 *       of your implementation.
 */
 
 // 0xA3 = 1010 0011
 // 0x58 = 0101 1000
 
unsigned int count_set_bits_in_array(unsigned char* array, unsigned int n) {
	unsigned int set_bits = 0;
	for (unsigned int a = 0; a < n; a++) { // Let's go through every byte.
		for (unsigned int b = 0; b < 8; b++) {
			if (array[a] & (1 << b)) { // This row has been a bit confusing.
				set_bits++;
			}
		}
	}
	return set_bits;
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
