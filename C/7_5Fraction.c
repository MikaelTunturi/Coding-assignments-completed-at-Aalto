#include "fraction.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Declare the structure fraction_st here

struct fraction_st {
    unsigned int o,n;
};

/**
 * \brief Calculates the greatest common divisor of two integers.
 *
 * \details This function finds the greatest common divisor of
 *          of integers u and v using Binary GCD algorithm
 *          See http://en.wikipedia.org/wiki/Binary_GCD_algorithm for
 *          the details.
 *
 * \param u The first integer
 * \param v The second integer
 * \return The greatest common divisor between u and v
 */

unsigned int gcd(unsigned int u, unsigned int v)
{
    // simple cases (termination)
    if (u == v)
        return u;
    if (u == 0)
        return v;
    if (v == 0)
        return u;
    // look for factors of 2
    if (~u & 1) // u is even
    {
        if (v & 1) // v is odd
            return gcd(u >> 1, v);
        else // both u and v are even
            return gcd(u >> 1, v >> 1) << 1;
    }
    if (~v & 1) // u is odd, v is even
        return gcd(u, v >> 1);
    // reduce larger argument
    if (u > v)
        return gcd((u - v) >> 1, v);
    return gcd((v - u) >> 1, u);
}

/**
 * \brief Allocates and initializes a Fraction object
 *
 * \param numerator The numerator of the fraction
 * \param denominator The denominator of the fraction
 * \return A pointer to the allocated fraction
 */

Fraction* setFraction(unsigned int numerator, unsigned int denominator)
{  
	Fraction *f = malloc(sizeof(struct fraction_st));
	f -> o = numerator;
	f -> n = denominator;
	return f;
}

/**
 * \brief Frees the memory of a fraction
 *
 * \param f The fraction to be freed.
 */

void freeFraction(Fraction* f)
{  
	assert(f);
	free(f);
}

/**
 * \brief Returns the numerator of the fraction f
 *
 * \param f The fraction
 * \return the numerator of f
 */

unsigned int getNum(const Fraction *f)
{  
	unsigned int num = f -> o;
	return num;
}

unsigned int getDenom(const Fraction *f)
{  
	unsigned int denom = f -> n;
	return denom;
}

int compFraction(const Fraction *a, const Fraction *b)
{  
	float num1 = a -> o;
	float denom1 = a -> n;
	float num2 = b -> o;
	float denom2 = b -> n;
	float f1 = num1 / denom1;
	float f2 = num2 / denom2;
	if(f1 < f2)
	{  
		return -1;
	}
	else if(f1 == f2)
	{  
		return 0;
	}
	else
	{  
		return 1;
	}
}

Fraction *addFraction(const Fraction *a, const Fraction *b)
{  
	Fraction *sum = malloc(sizeof(struct fraction_st));
	unsigned int num1 = getNum(a);
	unsigned int num2 = getNum(b);
	unsigned int den1 = getDenom(a);
	unsigned int den2 = getDenom(b);
	unsigned int den;
	if(den1 != den2)
	{  
		den = den1*den2;
		num1 = num1*den2;
		num2 = num2*den1;
	}
	else
	{  
		den = den1;
	}
	sum -> o = num1+num2;
	sum -> n = den;
	return sum;
}

void reduceFraction(Fraction *val)
{  
	unsigned int nume1 = val->o;
	unsigned int deno1 = val->n;
	unsigned int syn = gcd(nume1, deno1);
	val->o = nume1/syn;
	val->n = deno1/syn;
}