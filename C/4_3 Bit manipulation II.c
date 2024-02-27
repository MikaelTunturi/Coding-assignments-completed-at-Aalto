#include <stdio.h>

#define BIT_MASK1 ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))

#define BIT_MASK2 ((0 << 4) | (0 << 5) | (0 << 6) | (0 << 7))

unsigned char mergeBits(unsigned char a, unsigned char b) {
	unsigned char first = (a << 4);

	//unsigned char second = (b << 4);
	//second = (b >> 4);
	
	unsigned char second = b & ~BIT_MASK1;
	unsigned char merged_bits = first | second;
	return merged_bits;
}



