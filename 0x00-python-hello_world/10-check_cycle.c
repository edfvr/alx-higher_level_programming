#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: 
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;
	
	if (list == NULL)
		return 0;

	ptr1 = list;
	ptr2 = list;

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return 1;
	}

	return (0);
}
