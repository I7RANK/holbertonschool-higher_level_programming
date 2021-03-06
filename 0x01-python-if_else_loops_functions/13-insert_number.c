#include "lists.h"
#include <stdio.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: the header of the linked list
 * @number: the nomber to the new node to insert
 *
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *temp = NULL, *addresstemp = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	temp = *head;
	addresstemp = *head;

	while (temp != NULL)
	{
		if (temp->n >= new->n)
		{
			if (addresstemp == *head)
			{
				new->next = *head;
				*head = new;
				return (new);
			}
			new->next = addresstemp->next;
			addresstemp->next = new;
			return (new);
		}
		addresstemp = temp;
		temp = temp->next;
	}
	addresstemp->next = new;
	return (new);
}
