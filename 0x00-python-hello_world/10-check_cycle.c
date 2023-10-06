#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list contains a cycle
 * @list: singly linked list
 *
 * Return: 1 if there's a cycle, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	 if (list == NULL || list->next == NULL)
		 return (0);

	 x = list->next;
	 y = list->next->next;

	 while (x && y && y->next)
	 {
		 if (x == y)
			 return (1);

		 x = x->next;
		 y = y->next->next;
	 }
	 return (0);
}

