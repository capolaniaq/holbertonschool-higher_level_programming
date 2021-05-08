#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* is_palindrome - the function verify if the linked_list in palindrome
* @head: double pointer to indicate the head of linked list
*
* Return: 1 in case success or 0 in case failure
*/

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i = 0;
	int j = 0;
	char numbers[100];

	if (head == NULL)
		return (0);

	tmp = *head;
	while (tmp != NULL)
	{
		numbers[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	i--;
	while (j <= i)
	{
		if (numbers[j] != numbers[i])
			return (0);
		else if (j == i - 1)
			return (1);
		i--;
		j++;
	}
	return (0);
}
