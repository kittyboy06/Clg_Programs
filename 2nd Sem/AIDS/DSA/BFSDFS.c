#include <stdio.h>
#define MAX 5
int adj[MAX][MAX] = {
    {0,1,1,0,0},
    {1,0,0,1,0},
    {1,0,0,1,1},
    {0,1,1,0,1},
    {0,0,1,1,0}
};
int visited[MAX];
// DFS
void DFS(int v){
    visited[v]=1;
    printf("%d ",v);
    for(int i=0;i<MAX;i++)
        if(adj[v][i] && !visited[i])
            DFS(i);
}
// BFS
void BFS(int start){
    int queue[MAX], front=0, rear=0;
    int visitedB[MAX]={0};
    queue[rear++] = start;
    visitedB[start]=1;
    while(front<rear){
        int v=queue[front++];
        printf("%d ",v);
        for(int i=0;i<MAX;i++)
            if(adj[v][i] && !visitedB[i]){
                queue[rear++] = i;
                visitedB[i]=1;
            }
    }
}
int main(){
    printf("DFS Traversal: ");
    for(int i=0;i<MAX;i++) visited[i]=0;
    DFS(0);
    printf("\nBFS Traversal: ");
    BFS(0);
    printf("\n");
    return 0;
}
