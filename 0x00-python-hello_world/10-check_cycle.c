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
	int i, j;

	temp = list;
	temp2 = list;

	if (temp->next == NULL)
	{
		return (0);
	}

	for (i = 0; temp; i++)
	{
		for (j = 0; temp2; j++)
		{
			/* printf("temp == %p ==\ntemp2 == %p ==\n\n", (void *)temp, (void *)temp2); */
			if (temp == temp2 && j != i)
			{
				return (1);
			}
			temp2 = temp2->next;
		}
		temp = temp->next;
	}
	return (0);
}
