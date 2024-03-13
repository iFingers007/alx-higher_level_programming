#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check the list for cycle
 *@list: Linked list to be checked
 * Return: 1 if True, 0 if false.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list;
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
