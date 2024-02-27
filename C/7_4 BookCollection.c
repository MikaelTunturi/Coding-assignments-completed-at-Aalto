#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "book.h" //ks.tehtävänannon linkki

//varaa muistia jokaiselle kirjalle

int init_book(struct book *p_book, const char *p_id, const char *p_title, const char *p_author, struct date p_release)
{  if(strlen(p_id) >= 10)
  {  return 0;
  }

  unsigned int i;
  for(i=0; i<strlen(p_id); i++)
  {  p_book->id[i] = p_id[i];
  }
  p_book->id[i] = '\0';

  p_book->release_date.day = p_release.day;
  p_book->release_date.month = p_release.month;
  p_book->release_date.year = p_release.year;

  p_book->title = malloc(strlen(p_title)+1);
  p_book->author = malloc(strlen(p_author)+1);
  strcpy(p_book->title, p_title);
  strcpy(p_book->author, p_author);
  return 1;
}

struct book *add_to_collection(struct book *collection, unsigned int size, struct book new_book)
{  unsigned int i;
  for(i=0; i < size; i++);
  struct book *new_collection = realloc(collection, sizeof(struct book)*(i+2));  
  if (new_collection == NULL) 
  {       return NULL; // allocating memory did not work
      }  
  init_book(&new_collection[i], new_book.id, new_book.title, new_book.author, new_book.release_date);
/*  new_collection[i].title = new_book.title;
  new_collection[i].release_date.day = new_book.release_date.day;
  new_collection[i].release_date.month = new_book.release_date.month;
  new_collection[i].release_date.year = new_book.release_date.year;
  new_collection[i].author = new_book.author;
  new_collection[i].id = new_book.id;  */
  return new_collection;
}
