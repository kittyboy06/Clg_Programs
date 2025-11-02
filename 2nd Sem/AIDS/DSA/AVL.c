
#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node *left, *right;
    int height;
};
// Create new node
struct Node* newNode(int val){
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = val; n->left = n->right = NULL; n->height = 1;
    return n;
}
int height(struct Node* n){ return n ? n->height : 0; }
int max(int a,int b){ return a>b?a:b; }
// Rotations
struct Node* rightRotate(struct Node* y){
    struct Node* x=y->left; struct Node* T2=x->right;
    x->right=y; y->left=T2;
    y->height=1+max(height(y->left),height(y->right));
    x->height=1+max(height(x->left),height(x->right));
    return x;
}
struct Node* leftRotate(struct Node* x){
    struct Node* y=x->right; struct Node* T2=y->left;
    y->left=x; x->right=T2;
    x->height=1+max(height(x->left),height(x->right));
    y->height=1+max(height(y->left),height(y->right));
    return y;
}
int balance(struct Node* n){ return n ? height(n->left)-height(n->right) : 0; }
// Insert in AVL
struct Node* insert(struct Node* root,int key){
    if(!root) return newNode(key);
    if(key<root->data) root->left=insert(root->left,key);
    else if(key>root->data) root->right=insert(root->right,key);
    else return root;
    root->height=1+max(height(root->left),height(root->right));
    int b=balance(root);
    if(b>1 && key<root->left->data) return rightRotate(root);       // LL
    if(b<-1 && key>root->right->data) return leftRotate(root);      // RR
    if(b>1 && key>root->left->data){ root->left=leftRotate(root->left); return rightRotate(root); } // LR
    if(b<-1 && key<root->right->data){ root->right=rightRotate(root->right); return leftRotate(root); } // RL
    return root;
}
// Inorder traversal
void inorder(struct Node* root){
    if(root){ inorder(root->left); printf("%d ",root->data); inorder(root->right); }
}
int main(){
    struct Node* root=NULL;
    root=insert(root,30);
    root=insert(root,20);
    root=insert(root,40);
    root=insert(root,10);
    root=insert(root,25);
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    return 0;
}
