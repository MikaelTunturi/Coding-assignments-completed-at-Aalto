#include <stdio.h>
#include <math.h>

#include "source.h"

void simple_math(void)
{
	float num1, num2;
	char merkki;
	//char whitespace1, whitespace2;
	
	/*scanf("%f", &num1);
	scanf("%s", &whitespace1);
	scanf("%c", &merkki);
	scanf("%s", &whitespace2);
	scanf("%f", &num2);*/
	
	scanf("%f %c %f", &num1, &merkki, &num2);
	
	// miten whitespacet????
	
	// mitä seuraavaan if:iin????
	
	if (num1) { // MUISTA SULUT IF-LAUSEEN YHTEYDESSÄ.
		if (num2) {
			if (merkki == '+' || merkki == '-' || merkki == '*' || merkki == '/') {
			//if &merkki == '+' || &merkki == '-' || &merkki == '*' || &merkki == '/' {
				if (merkki == '+') {
					float tulos = num1 + num2;
					printf("%.1f\n", tulos); // TULOSTUKSEEN RIVINVAIHTO.
				}
				else if (merkki == '-') {
					float tulos = num1 - num2;
					printf("%.1f\n", tulos);
				}
				else if (merkki == '*') {
					float tulos = num1 * num2;
					printf("%.1f\n", tulos);
				}
				else {
					float tulos = num1 / num2;
					printf("%.1f\n", tulos);
				}
			}
			else {
				printf("ERR\n");
			}
		}
		else {
			printf("ERR\n");
		}
	}	
	else {
		printf("ERR\n");
	}
	//return 0;
}