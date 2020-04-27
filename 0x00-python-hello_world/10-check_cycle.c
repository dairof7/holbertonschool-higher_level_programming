#include "lists.h"

/**
 * check_cycle - check if is circle list
 * @list: head of the list
 * Return: 1 if list is circular and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;



	temp = list;
	while (temp->next != NULL, list == NULL)
	{
		if (list == temp->next)
			return (1);
		temp = temp->next;
	}
	return (0);
}
