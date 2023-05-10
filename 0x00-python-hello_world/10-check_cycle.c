#include "lists.h"

/**
 * check_cycle - A function that checks if a linked list contains a cycle
 * @list: parameter of the linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* Declare two pointers to traverse the list */
	listint_t *tortoise = list;
	listint_t *hare = list;

	/* If the list is empty, return 0 (no cycle) */
	if (!list)
		return (0);

	/* Traverse the list with two pointers (tortoise and hare) */
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next; /* Move the tortoise one step */
		hare = hare->next->next; /* Move the hare two steps */

		/* If the two pointers meet, there is a cycle in the list */
		if (tortoise == hare)

			return (1);
	}

	/* If the traversal completes without finding a cycle, return 0 */
	return (0);
}

