#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/**
 * \brief Converts all punctuation characters in a null-terminated 
 *        string to space character, ' '.
 * 
 * \details This function finds all punctuation characters in a string and 
 *          converts these characters into a space character, ' '. It changes 
 *          the found punctuation characters inplace so that no dynamic 
 *          allocation is needed.
 * 
 * \param str The null-terminated string with some punctuation characters.
 * 
 * \note stdlib provides useful character handling functions in ctype.h. 
 *       ctype.h documentation also states different character classes,  
 *       including punctuation characters.
 * 
 * \note In your implementation, do not write to stdout to check the functionality.
 *       You should use my_tests function to print and check the functionality 
 *       of your implementation.
 */
void convert_punctuation(char* str) {
	//TODO: implement your function here!
	for (long unsigned int i = 0; i < strlen(str); i++) {	
		if (ispunct(str[i])) {
			str[i] = ' ';
		}
	}
}

void my_tests(void) {
	// You can write your own test code here.
}

int main(void) {
	/* You may implement your own tests in my_tests function */
	my_tests();
	return 0;
}