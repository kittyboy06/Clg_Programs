#include <iostream>
using namespace std;
struct CircularLinkedList {
    int data;
    CircularLinkedList* next;
}*head, *temp, *newNode;
void createNode(int value)
{
    newNode = (struct CircularLinkedList*)malloc(sizeof(struct CircularLinkedList));
    newNode->data = value;
    newNode->next = head;

    if (head == nullptr) {
        head = newNode;
        newNode->next = head;
    } else {
        temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void insertAtPosition(int value, int position) {
    newNode = (struct CircularLinkedList*)malloc(sizeof(struct CircularLinkedList));
    newNode->data = value;

    if (position == 1) 
    {
        newNode->next = head;
        temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        head = newNode; 
    } 
    else 
    {
        temp = head;
        for (int i = 1; i < position - 1 && temp->next != head; i++) 
        {
            temp = temp->next;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void display()
{
    if (head == nullptr) return;
    temp = head;
    do {
        cout << temp->data << " ";
        temp = temp->next;
    } while (temp != head);
    cout << endl;
}

void deleteAtPosition(int position) {
    if (head == nullptr) return;

    temp = head;

    if (position == 1) {
        if (head->next == head) {
            free(head);
            head = nullptr;
        } else {
            while (temp->next != head) {
                temp = temp->next;
            }
            CircularLinkedList* toDelete = head;
            temp->next = head->next;
            head = head->next;
            free(toDelete);
        }
        return;
    }

    for (int i = 1; temp->next != head && i < position - 1; i++) {
        temp = temp->next;
    }
    if (temp->next == head) return;

    CircularLinkedList* toDelete = temp->next;
    temp->next = toDelete->next;
    free(toDelete);
}

int main()
{
    head = nullptr;
    createNode(10);
    createNode(20);
    createNode(30);
    cout << "Circular Linked List: ";
    display();

    insertAtPosition(15, 2);
    cout << "After inserting 15 at position 2: ";
    display();

    deleteAtPosition(3);
    cout << "After deleting node at position 3: ";
    display();

    return 0;
}