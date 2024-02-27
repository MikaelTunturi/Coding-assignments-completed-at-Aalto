#include "stringsplit.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/**
 * \brief Splits a string into its parts, and returns a dynamically allocated  
 *        array of strings that are dynamically allocated.
 * 
 * \details For example called with "Test string split" and " ",
 *          the function returns ["Test", "string", "split", NULL].
 *          
 *          Or called with "Another - test" and " - ",
 *          returns ["Another", "test", NULL].
 * 
 * \param str The null-terminated string to split.
 * \param split The token string to split str with.
 * \return An array of strings that contains parts of str in each of 
 *         strings excluding the split.      
 */
char** split_string(const char* str, const char* split) {
	int all_str = sizeof(char*);
	char** new_str = malloc(all_str);
	char* gap = strstr(str, split);
	
	int a = 0;
	
	while (gap != NULL) {
		all_str += sizeof(char*);
		new_str = realloc(new_str, all_str);
		new_str[a] = malloc(strlen(str) - strlen(gap) + 1);
		strncpy(new_str[a], str, gap-str);
		new_str[a][gap-str] = 0;
		
		str = gap + strlen(split);
		gap += strlen(split);
		a += 1;
		gap = strstr(str, split);
	}
	if (gap == NULL) {
		all_str += sizeof(char*);
		new_str = realloc(new_str, all_str);
		new_str[a] = malloc(strlen(str) + 1);
		strncpy(new_str[a], str, strlen(str));
		new_str[a][strlen(str)] = 0;
	}
	new_str[a+1] = NULL;
	return new_str;
}

/**
 * \brief Prints string parts that are split with split_string function.
 * 
 * \param split_string An array of strings returned by split_string function.
 */
void print_split_string(char** split_string) {
	/*for (int i = 0; i < strlen(split_string); i++) {
		printf("%c\n", split_string[i]);
	}*/
	int a = 0;
	while (split_string[a] != NULL) {
		printf("%s\n", split_string[a]);
		a++;
	}
}

/**
 * \brief Releases dynamically allocated string parts by split_string function.
 * 
 * \param split_string An array of strings returned by split_string function.
 */
void free_split_string(char** split_string) {
	/*for (int i = 0; i < strlen(split_string); i++) {
		free(split_string[i]);
	}
	free(split_string);*/
	int a = 0;
	while (split_string[a] != NULL) {
		free(split_string[a]);
		a++;
	}
	free(split_string);
}
