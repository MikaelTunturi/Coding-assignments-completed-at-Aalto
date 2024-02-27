#include <stdio.h>
#include <math.h>

double vectorlength(double x, double y, double z)
{
	// Let's calculate the square root of the sum of each element's square.
	double res = sqrt(pow(x,2) + pow(y,2) + pow(z,2));
	return res;
}
