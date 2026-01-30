#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};	
// Create new node
struct Node* newNode(int val){
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = val;
    n->left = n->right = NULL;
    return n;
}
// Insert in BST
struct Node* insert(struct Node* root, int val){
    if(!root) return newNode(val);
    if(val < root->data) root->left = insert(root->left, val);
    else root->right = insert(root->right, val);
    return root;
}
// Inorder traversal
void inorder(struct Node* root){
    if(root){
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
int main(){
    struct Node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    return 0;
}
