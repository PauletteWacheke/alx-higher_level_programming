#include "lists.h"

/**
 * is_palindrome - function that checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list.
 *
 * Return: 1 if linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *init = *head;
	int size[2048], i = 0, j = 0;

	if (*head)
	{
		while (init)
		{
			size[i] = init->n;
			init = init->next;
			i++;
		}

		while (j < i / 2)
		{
			if (size[j] == size[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
