#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
* insert_node - function that insert one a node in sort of the number
* @head: double pointer to head of the linked list
* @number: int to insert in the new node
*
* Return: new node inserted
**/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	listint_t *tmp2;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	tmp = *head;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (new->n <= tmp->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	tmp2 = tmp->next;
	while  (tmp2->next != NULL)
	{
		if (tmp->n <= new->n && tmp2->n >= new->n)
		{
			tmp->next = new;
			new->next = tmp2;
			new = new->next;
			return (new);
		}
		tmp = tmp->next;
		tmp2 = tmp2->next;
	}
	tmp2->next = new;
	return (new);
}
