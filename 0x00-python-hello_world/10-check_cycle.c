#include "lists.h"

/**
 * check_cycle - function that checks if list has cycle
 * @list: pointer to list to check
 *
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
	{
		return (0);
	}

	while (list)
	{
		temp = list;
		list = list->next;

		if (temp <= list)
		{
			return (1);
		}
	}
	return (0);
}
