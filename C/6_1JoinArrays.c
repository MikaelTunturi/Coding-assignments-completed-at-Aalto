#include <stdio.h>
#include <stdlib.h> // malloc- ja free-funktiot
#include <stdint.h>

// Järjestys:
// 1. Määritetään datan tallentamiseen vaaditun muistin koko.
// 2. Varataan saatavilla olevasta muistista juuri oikean kokoinen alue.
// 3. Tarkistetaan onnistuiko muistin varaaminen.
// 4. Tallennetaan data varattuun muistiin ja prosessoidaan se.
// 5. Vapautetaan varattu muisti, jotta muut ohjelman osat tai muut 
// ohjelmat pääsevät käyttämään sitä omiin tarkoituksiinsa.

// muistivuotojen välttäminen -> pitkän aikavälin vaikutus

// calloc-funktion palauttama muisti on alustettu nollilla

// realloc-funktio: ensimmäinen parametri on osoitin aiemmin varattuun
// muistilohkoon & toinen parametri on lohkon uusi koko
// void* realloc(void*, size_t);

// funktio voi siirtää muistilohkon uuteen sijaintiin, jonka osoite palautetaan
// HUOM! Jos realloc siirtää muistilohkon uuteen sijaintiin:
	// 1. se varaa annetun määrän muistia
	// 2. se kopioi datan aikaisemmin varatusta muistilohkosta uuteen
	// 3. se vapauttaa aikaisemman muistilohkon
// Siispä prosessointikulut ovat hieman suuremmat, mutta joskus funktiolle
// käyttöä.

/*
int main_realloc(void) {
	int *table;
	table malloc(100*sizeof(int));
	if (table == NULL) {
		return -1;
	}
	int i;
	for (i = 0; i < 100; i++) {
		table[i] = 100 - 1;
	}
	int *newtable = realloc(table, 200*sizeof(int));
	if (!newtable) {
		free(table);
		return -1;
	}
	else {
		for (i = 100; i < 200; i++) {
			newtable[i] = 100 - 1;
		}
		for (i = 0; i < 200; i++) {
			printf("%d ", newtable[i]);
			if (!(i % 20)) {
				printf("\n");
			}
		}
		free(newtable);
	}
	return 0;
}
*/

#include "source.h"

/**
 * \brief Joins 3 arrays into a new dynamically allocated array
 *
 * \param n1 The number of elements in array
 * \param a1 The array 1 composed of n1 elements
 * \param n2 The number of elements in array
 * \param a2 The array 1 composed of n1 elements
 * \param n3 The number of elements in array
 * \param a3 The array 1 composed of n1 elements
 * \return a pointer to the dynamically allocated array
 *
 * \note The caller is responsible for deallocating the allocated array
 */
int *join_arrays(unsigned int n1,
                 const int *a1,
                 unsigned int n2,
                 const int *a2,
                 unsigned int n3,
                 const int *a3)
{
    unsigned int n_total = n1+n2+n3; // herjaako, jos ei ole unsigned int?
	int *joined = malloc((n_total)*sizeof(unsigned int));
	/*if (joined == NULL) {
		return -1; // ei ole kyllä int* --> luultavasti ei tarvii tätä ehtoa
	}*/
	for (unsigned int i = 0; i < n1; i++) {
		joined[i] = a1[i];
	}
	// käytetään indeksiä i edellisestä
	for (unsigned int j = 0, i = (n1); j < n2; j++, i++) {
		joined[i] = a2[j];
	}
	for (unsigned int k = 0, i = (n1+n2); k < n3; k++, i++) {
		joined[i] = a3[k];
	}
	return joined;
}