#include <stdio.h>

// numerator = osoittaja
// (de)nominator = nimittäjä

double fracsum(int x, int y, int a, int b) {
	double frac1 = (double) x/y;
	double frac2 = (double) a/b;
	double res = frac1 + frac2;
	return res;
}
