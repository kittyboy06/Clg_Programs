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

void Insert_Middle(int x,int p)
{
    NewNode = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    NewNode->data = x;
    while (Temp -> next != NULL)
    {
        for (int i = 0; i < p - 1; i++)
        {
            Temp = Temp->next;
        }
        NewNode->next = Temp->next;
        Temp->next = NewNode;
    }
    Temp = List;
    
}

int main()
{
    return 0;
}