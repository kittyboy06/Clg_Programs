#include <iostream>
using namespace std;
struct Node {
    int data;
    Node *left, *right;
    int height;
};

struct Node* newNode(int val) {
    Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = val; n->left = n->right = NULL; n->height = 1;
    return n;
}

int height(Node* n) { return n ? n->height : 0; }
int max(int a, int b) { return a > b ? a : b; }

Node* rightRotate(Node* y) {
    Node* x = y->left; Node* T2 = x->right;
    x->right = y; y->left = T2;
    y->height = 1 + max(height(y->left), height(y->right));
    x->height = 1 + max(height(x->left), height(x->right));
    return x;
}

Node* leftRotate(Node* x) {
    Node* y = x->right; Node* T2 = y->left;
    y->left = x; x->right = T2;
    x->height = 1 + max(height(x->left), height(x->right));
    y->height = 1 + max(height(y->left), height(y->right));
    return y;
}

int balance(Node* n) { return n ? height(n->left) - height(n->right) : 0; }

Node* insert(Node* root, int key) {
    if (!root) return newNode(key);
    if (key < root->data) root->left = insert(root->left, key);
    else if (key > root->data) root->right = insert(root->right, key);
    else return root;
    root->height = 1 + max(height(root->left), height(root->right));
    int b = balance(root);
    if (b > 1 && key < root->left->data) return rightRotate(root);       // LL
    if (b < -1 && key > root->right->data) return leftRotate(root);      // RR
    if (b > 1 && key > root->left->data) { root->left = leftRotate(root->left); return rightRotate(root); } // LR
    if (b < -1 && key < root->right->data) { root->right = rightRotate(root->right); return leftRotate(root); } // RL
    return root;
}   

void inorder(Node* root) {
    if (root) { inorder(root->left); printf("%d ", root->data); inorder(root->right); }
}

int main() {
    Node* root = NULL;
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 10);
    root = insert(root, 25);
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    return 0;
}