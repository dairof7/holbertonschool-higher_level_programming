#include "lists.h"

/**
 * check_cycle - check if is circle list
 * @list: head of the list
 * Return: 1 if list is circular and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	temp1 = list;
	temp2 = list;
	while (temp1 != NULL && temp2 != NULL && temp2 != NULL)
	{
		temp1 = temp1->next;
		temp2 = temp2->next;
		temp2 = temp2->next;
		if (temp1 == temp2)
			return (1);
	}
	return (0);
}
