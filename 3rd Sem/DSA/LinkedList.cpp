#include<iostream>
using namespace std;

struct LinkedList {
    int data;
    LinkedList* next;
}*List,*Next,*NewNode,*Temp;

void Create()
{
    List = NULL;
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    cout << "Enter the elements of the linked list: ";
    cin>> NewNode->data;
    NewNode->next = NULL;
    List = NewNode;
    Temp = List;
}

void Insert_Beginning(int x)
{
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    NewNode->data = x;
    NewNode->next = List;
    List = NewNode;
}

void display()
{
    Temp = List;
    while (Temp != NULL)
    {
        cout << Temp->data << " ";
        Temp = Temp->next;
    }
    cout << endl;
}

void deleteAtPosition(int position) {
    if (List == nullptr) return;

    Temp = List;

    if (position == 1) {
        List = Temp->next;
        free(Temp);
        return;
    }

    for (int i = 1; Temp != nullptr && i < position - 1; i++) {
        Temp = Temp->next;
    }
    if (Temp == nullptr || Temp->next == nullptr) return;

    Next = Temp->next->next;
    free(Temp->next);
    Temp->next = Next;
}

void Insert_End(int x)
{
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    NewNode->data = x;
    NewNode->next = NULL;
    if (List == NULL) {
        List = NewNode;
    } else {
        Temp = List;
        while (Temp->next != NULL) {
            Temp = Temp->next;
        }
        Temp->next = NewNode;
    }
}

void Insert_Middle()
{
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    int p;
    cout << "Enter the position to insert the new node: ";
    cin >> p;
    cout << "Enter the element to insert in the middle: ";
    cin >> NewNode->data;
    NewNode->next = NULL;

    if (List == NULL) {
        List = NewNode;
    } else {
        Temp = List;
        for (int i = 1; i < p - 1 && Temp != NULL; i++) {
            Temp = Temp->next;
        }
        NewNode->next = Temp->next;
        Temp->next = NewNode;
    }
    Temp = List;
    
}

int main()
{
    Create();
    Insert_Beginning(5);
    display();
    return 0;
}