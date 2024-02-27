#include <stdio.h>

# define BIT_MASK ((1 << 0) | (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))

# define BIT_MASK2 ((1 << 6) | (1 << 7))

unsigned char sixBits(unsigned char v) {
	unsigned char palautus = v & ~BIT_MASK2;
	return palautus;
}
