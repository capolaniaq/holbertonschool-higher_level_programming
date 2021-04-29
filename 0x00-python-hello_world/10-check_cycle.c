#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
* check_cycle - function that verify if teh linked_list is cycle
* @list: head of the list
*
* Return: 1 in case success and 0 if failure case
**/

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;

		if (turtle == hare)
			return (1);
	}
	return (0);
}
