#include "lists.h"

/**
 * check_cycle - checks if the simple linked list have a cycle
 * @list: the header of the simple linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;
	int i;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	temp = list->next;
	temp2 = list;

	for (i = 0; temp; i++)
	{
		if (temp == temp2)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
