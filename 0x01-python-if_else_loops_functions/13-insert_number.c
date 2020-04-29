#include "lists.h"

/**
 * insert_node - insert a node in a linked list.
 * checking the number
 * @head: the head of the list
 * @number: the number to add in the new node
 * Return: the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *_next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	current = *head;
	_next = current->next;
	while (current)
	{
		if (number <= current->n)
		{
			new->next = *head;
			*head =  new;
			return (new);
		}
		if ((current->next == NULL) && (number >= current->n))
		{
			current->next = new;
			new->next = NULL;
			return (new);
		}
		if ((number >= current->n) && (number <= _next->n))
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
		_next = current->next;
	}
	return (NULL);
}
