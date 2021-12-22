#include "lists.h"
#include "stdlib.h"

/**
 * insert_node - function that inserts a number into a sorted list
 * @head: pointer to the head of the list
 * @number: number
 * Return: pointer or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *insert_node;

	current = *head;

	while (current->next != NULL)
	{
		if (current->n <= number && number <= current->next->n)
		{
			insert_node = malloc(sizeof(listint_t));
			if (insert_node == NULL)
				return (NULL);

			insert_node->n = number;
			insert_node->next = current->next;
			current->next = insert_node;
			break;
		}
		current = current->next;
	}
	return (insert_node);
}
