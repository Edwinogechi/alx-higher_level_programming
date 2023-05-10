#include "lists.h"

/**
 * insert_node - Function inserting a number to a sorted singly-linked list.
 * @head: Pointer parameter to the head of the linked list.
 * @number: Number parameter to be inserted.
 *
 * Return: the address of the new node
 * Otherwise - NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* Declare pointers to traverse and insert nodes */
	listint_t *node = *head, *new_node;

	 /* Allocate memory for new node created */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	/* Initialize the new node with the given data */
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		/* Insert the new node at the beginning of the list */
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list until the correct position for the new node is found */
	while (node && node->next && node->next->n < number)
		node = node->next;

	/* Insert the new node in the correct position */
	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
