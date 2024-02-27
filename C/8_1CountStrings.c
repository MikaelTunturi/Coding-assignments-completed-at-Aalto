#include "source.h"

#include <stdio.h>
#include <string.h>

/**
 * \brief Returns the number of occurrences of string sub in the string str.
 * 
 * \param str A null-terminated string that might contain sub in it. 
 * \param sub A null terminated string to search for.
 * \return The number of occurrences of sub in str.
 * 
 * \note strstr function declared in string.h might be useful. 
 */
int num_substr(const char* str, const char* sub) {
	int count = 0;
	//int sub_length = strlen(sub);
	//int sub_count = 0;
	char * to_find = strstr(str, sub); // pointteri ensimmäisen sub:iin
	
	for (long unsigned int i = 0; i < strlen(str); i++) {
		// käydään str läpi
		if (to_find != NULL) {
			count++;
		}
		for (long unsigned int a = 0; a < strlen(sub); a++) {
			str++;
		}
		to_find = strstr(str, sub);
	}
	return count/2;
}
/*if (strcmp(strstr(str, sub)) > 0) {
			sub_count++;
		}
		if (sub_count == sub_length) {
			count++;
		}*/
		
		//something = strstr(str, sub);
		/*if (something != NULL) {
			if (something == sub) {
				count++;
			}
		}*/