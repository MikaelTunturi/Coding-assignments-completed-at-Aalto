#include <stdio.h>
#include <math.h>

void draw_triangle(unsigned int size) {
	for (unsigned int a = 0; a < size; a++) {
		for (unsigned int b = 0; b < (size-1-a); b++) {
			printf(".");
		}
		for (unsigned int c = 0; c < a+1; c++) {
			printf("#");
		}
		printf("\n");
	}
}
