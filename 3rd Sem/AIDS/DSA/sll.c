#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
int main() {
    struct Node* head,*sec,*thi,*prev,*temp;
    head = (struct Node*)malloc(sizeof(struct Node));
    sec = (struct Node*)malloc(sizeof(struct Node));
    thi = (struct Node*)malloc(sizeof(struct Node));
    head->data = 1;
    sec->data = 2;
    thi->data = 3;
    head->next = sec;
    sec->next = thi;
    thi->next = NULL;
    temp = head;

    while (temp->data != 2) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = temp->next;
    free(temp);

    temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    return 0;
}