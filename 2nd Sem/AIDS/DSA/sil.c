#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;
void insert(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = NULL;
    if (head == NULL) head = newNode;
    else {
        struct Node* temp = head;
        while (temp->next) temp = temp->next;
        temp->next = newNode;
    }
    printf("%d inserted\n", val);
}
void delet(int val) {
    struct Node *temp = head, *prev = NULL;
    while (temp && temp->data != val) {
        prev = temp;
        temp = temp->next;
    }
    if (!temp) { printf("%d not found\n", val); return; }
    if (!prev) head = head->next;
    else prev->next = temp->next;
    free(temp);
    printf("%d deleted\n", val);
}
void search(int val) {
    struct Node* temp = head;
    int pos = 1;
    while (temp) {
        if (temp->data == val) { printf("%d found at position %d\n", val, pos); return; }
        temp = temp->next; pos++;
    }
    printf("%d not found\n", val);
}
void display() {
    struct Node* temp = head;
    if (!temp) { printf("List empty\n"); return; }
    printf("List: ");
    while (temp) { printf("%d ", temp->data); temp = temp->next; }
    printf("\n");
}
int main() {
    insert(10); insert(20); insert(30);
    display();
    search(20);
    delet(10);
    display();
    return 0;
}
