#include<iostream>

struct doubleLinkedList
{
    int data;
    doubleLinkedList* next;
    doubleLinkedList* prev;
}*head, *tail, *temp, *newNode;

void createNode(int value)
{
    newNode = (struct doubleLinkedList*)malloc(sizeof(struct doubleLinkedList));
    newNode->data = value;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if (head == nullptr) {
        head = tail = newNode;
    } else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
}

void insertAtPosition(int value, int position) {
    newNode = (struct doubleLinkedList*)malloc(sizeof(struct doubleLinkedList));
    temp = head;
    newNode->data = value;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if (position == 1) 
    {
        newNode->next = head;
        if (temp->prev == nullptr) 
        {
            head->prev = newNode;
        }
        head = newNode; 
    }

    temp = head;
    for (int i = 0; i < position && temp != nullptr; i++) 
    {
        temp = temp->next;
    }
    
    newNode->next = temp;
    newNode->prev = temp;
    temp->next = newNode;
    if (newNode->next != nullptr) {
        newNode->next->prev = newNode;
    } else {
        tail = newNode;
    }
}