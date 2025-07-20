#include<iostream>
using namespace std;

struct LinkedList {
    int data;
    LinkedList* next;
}*List,*Next,*NewNode,*Temp;

void Create(int n)
{
    int x;
    List = NULL;
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    cout << "Enter the elements of the linked list: ";
    cin>> x;
    NewNode->data = x;
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

int main()
{
    return 0;
}