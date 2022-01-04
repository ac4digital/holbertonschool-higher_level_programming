#include <stddef.h>
#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - function that identifies if a string is palindrome or not
 * @head: pointer to list to check
 * Return: 0 if is not palindrome otherwise 1
 */

int is_palindrome(listint_t **head)
{
    listint_t *current;
    int i, length = 1;
    int *copy_list;
    
    current = *head;

    if (current == NULL)
        return (1);
    
    while (current->next != NULL)
    {
        current = current->next;
        length++;
    }
    copy_list = malloc(sizeof(int) * length);
    if (copy_list == NULL)
        exit(98);
    current = *head;

    for (i = (length - 1); i >= 0; i--)
    {
        copy_list[i] = current->n;
        current = current->next;
    }
    current = *head;
    for (i = 0; i < length; i++)
    {
        if (copy_list[i] != current->n)
            return (0);
    current = current->next;
    }
    free(copy_list);
    return (1);
}
