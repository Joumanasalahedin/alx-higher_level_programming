#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *reversed_second_half = reverse_list(slow);
	listint_t *original_first_half = *head;

	while (reversed_second_half != NULL)
	{
		if (original_first_half->n != reversed_second_half->n)
			return (0);

		original_first_half = original_first_half->next;
		reversed_second_half = reversed_second_half->next
	}
	return (1);
}
