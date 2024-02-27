#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define BIT_MASK (1 << i)

// TÄMÄ TAPA MENI LOPULTA OIKEIN, KUN MUUTIN FUNKTIOIDEN 
// OP_BIT_SET, _CLEAR JA _TOGGLE PALAUTUSTYYPIN VOIDISTA 
// MUOTOON UINT32_T JA FUNKTION LOPPUUN RETURN DATA.

// TUSKAILIN AIVAN LIIAN PITKÄÄN TÄMÄN TEHTÄVÄN KANSSA, VAIKKA
// TÄMÄ OLISI OLLUT OIKEIN. TEHTÄVÄN OHJEISTUS VOID-MUODOSTA OLI
// TODELLA HARHAANJOHTAVA. VALMIISSA POHJISSA OLI PALAUTUSMUOTO
// TÄYSIN ERI.

// VOISI PERIAATTEESSA VALITTAA, SILLÄ TÄMÄ JOHTI VÄHEMPIIN PISTEI-
// SIIN MUTTA TOISAALTA EN JAKSA VAIVAUTUA. MENEN LUULTAVASTI NÄIN
// ETEENPÄIN SEURAAVIA TEHTÄVIÄ KOHTI.

void op_print_byte(unsigned char b) { //Oikein!
	for (int i = 7; i >= 0; i--) {
		if (b & (1 << i)) {
			printf("1");
		}
		else {
			printf("0");
		}
	}
}

uint32_t op_bit_set(uint32_t data, int i) {
	/*for (int a = 0; a < 32; a++) {
		if (a == i) {
			data = data | (1 << a);
		}
	}*/
	//data = data & BIT_MASK;
	uint32_t data_2 = 0x00000000;
	data_2 = data_2 | BIT_MASK;
	data = data | data_2;
	return data;
}

uint32_t op_bit_clear(uint32_t data, int i) {
	//uint32_t data_2 = data;
	for (int a = 0; a < 32; a++) {
		if (a == i) {
			data = data & ~(1 << a);
		}
	}
	//data = data & ~(1 << i);
	return data;
}

uint32_t op_bit_toggle(uint32_t data, int i) {
	//uint32_t data_2 = data;
	for (int a = 0; a < 32; a++) {
		if (a == i) {
			data = data ^ (1 << i);
		}
	}
	//data = data ^ (1 << i);
	return data;
}

uint8_t op_bit_get(uint32_t data, int i) { //Oikein!
	for (int a = 0; a < 32; a++) {
		if (a == i) {
			if (data & (1 << a)) {
				return 1;
			}
			else {
				return 0;
			}
		}
	}
	return 0;
}