#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if the linked list is a palindrome
 * @head: the header
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int j = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	return (checks_palin(*head, *head, 0, &j));
}

/**
 * checks_palin - checks if the linked list is a palindrome
 * @left_t: a pointer runs from left to right
 * @right_t: a pointer runs from right to left
 * @i: the position of @right
 * @j: the index to which @left should move
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int checks_palin(listint_t *left_t, listint_t *right_t, int i, int *j)
{
	int ret = 1;

	if (right_t->next != NULL)
	{
		ret = checks_palin(left_t, right_t->next, i + 1, j);
	}
	if (ret == 0)
	{
		return (ret);
	}

	/* if *j is subtracted with i is equals to de index to @left */
	if (right_t->next == NULL)
	{
		*j = i;
	}
	i = *j - i;

	while (i > 0)
	{
		left_t = left_t->next;
		i--;
	}

	if (right_t->n != left_t->n)
	{
		return (0);
	}

	return (1);
}
