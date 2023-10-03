#ifndef _LIST_H_
#define _LIST_H_

/* Libraries */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* struct */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* prototypes */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
