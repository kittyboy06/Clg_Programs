#include<iostream>
using namespace std;
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
    for (int i = 0; i <= position - 1 && temp != nullptr; i++) 
    {
        temp = temp->next;
    }
    newNode->next = temp;
    newNode->prev = temp->prev;
    if (temp->prev != nullptr) 
    {
        temp->prev->next = newNode;
    }
    temp->prev = newNode;
}

void display()
{
    temp = head;
    while (temp != nullptr)
    {
        cout<< temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void deleteAtLast() {
    if (tail == nullptr) return;

    temp = tail;

    if (tail->prev != nullptr) {
        tail = tail->prev;
        tail->next = nullptr;
    } else {
        head = tail = nullptr;
    }
    free(temp);
}

void Insert_End(int x)
{
    newNode = (struct doubleLinkedList*)malloc(sizeof(struct doubleLinkedList));
    newNode->data = x;
    newNode->next = nullptr;
    newNode->prev = tail;

    if (tail != nullptr) {
        tail->next = newNode;
    }
    tail = newNode;

    if (head == nullptr) {
        head = tail;
    }
}

void deleteAtPosition(int position) {
    if (head == nullptr) return;

    temp = head;

    if (position == 1) {
        head = temp->next;
        if (head != nullptr) {
            head->prev = nullptr;
        } else {
            tail = nullptr;
        }
        free(temp);
        return;
    }

    for (int i = 1; temp != nullptr && i < position; i++) {
        temp = temp->next;
    }
    if (temp == nullptr) return;

    if (temp->next != nullptr) {
        temp->next->prev = temp->prev;
    } else {
        tail = temp->prev;
    }
    if (temp->prev != nullptr) {
        temp->prev->next = temp->next;
    }
    free(temp);
}

int main()
{
    createNode(10);
    createNode(20);
    createNode(30);
    display();

    insertAtPosition(15, 2);
    display();

    deleteAtLast();
    display();

    Insert_End(40);
    display();

    return 0;
}