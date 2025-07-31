#include<iostream>
#include<conio.h>
using namespace std;

int cheat[] = {0,0,0,0,0,0,0,0,0};
char X_O[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
int a = 1;

void check()
{
    if((X_O[0] == X_O[1] && X_O[1] == X_O[2] == 'X') ||
       (X_O[3] == X_O[4] && X_O[4] == X_O[5] == 'X') ||
       (X_O[6] == X_O[7] && X_O[7] == X_O[8] == 'X') ||
       (X_O[0] == X_O[3] && X_O[3] == X_O[6] == 'X') ||
       (X_O[1] == X_O[4] && X_O[4] == X_O[7] == 'X') ||
       (X_O[2] == X_O[5] && X_O[5] == X_O[8] == 'X') ||
       (X_O[0] == X_O[4] && X_O[4] == X_O[8] == 'X') ||
       (X_O[2] == X_O[4] && X_O[4] == X_O[6] == 'X'))
    {
        X_Wins();
    }
    else if((X_O[0] == X_O[1] && X_O[1] == X_O[2] == 'O') ||
            (X_O[3] == X_O[4] && X_O[4] == X_O[5] == 'O') ||
            (X_O[6] == X_O[7] && X_O[7] == X_O[8] == 'O') ||
            (X_O[0] == X_O[3] && X_O[3] == X_O[6] == 'O') ||
            (X_O[1] == X_O[4] && X_O[4] == X_O[7] == 'O') ||
            (X_O[2] == X_O[5] && X_O[5] == X_O[8] == 'O') ||
            (X_O[0] == X_O[4] && X_O[4] == X_O[8] == 'O') ||
            (X_O[2] == X_O[4] && X_O[4] == X_O[6] == 'O'))
    {
        O_Wins();
    }
}

void X_Wins()
{
    out();
    cout<<"Player X wins!"<<endl;
    gameover();
}

void O_Wins()
{
    out();
    cout<<"Player O wins!"<<endl;
    gameover();
}

void Cheat_Check(int x)
{
    if(cheat[x-1] == 0)
    {
        cheat[x-1] = 1;
    }
    else
    {
        cout<<"Cheat Detected!"<<endl;
        start();
    }
}

void inva()
{
    cout<<"Enter a Value"<<endl;
    start();
}

void X_mark(x)
{
    X_O[x-1] = 'X';
    start();
}

void O_mark(x)
{
    X_O[x-1] = 'O';
    start();
}

void check_val(int x)
{
    if(x<0 || x>10)
    {
        cout<<"Invalid Value"<<endl;
        start();
    }
}

void start()
{
    if(a == 10)
    {
        gameover();
    }
    else if (a % 2 != 0)
    {
        check();
        clrscr();
        cout<<"Player X's Turn"<<endl;
        out();
        int pos = 0;
        cout<<"Enter Position (1-9): ";
        cin>>pos;
        check_val(pos);
        Cheat_Check(pos);
        a+=1;
        mark_X(pos);
    }
    else if (a % 2 == 0)
    {
        check();
        clrscr();
        cout<<"Player O's Turn"<<endl;
        out();
        int pos = 0;
        cout<<"Enter Position (1-9): ";
        cin>>pos;
        check_val(pos);
        Cheat_Check(pos);
        a+=1;
        mark_O(pos);
    }
    
}

void gameover()
{
    cout<<"Game Over!"<<endl;
    menu();
}

void out()
{
    printf("  %c  |  %c  |  %c  \n────────────────\n  %c  |  %c  |  %c  \n────────────────\n  %c  |  %c  |  %c  \n", X_O[0], X_O[1], X_O[2], X_O[3], X_O[4], X_O[5], X_O[6], X_O[7], X_O[8]);
}

void menu()
{
    cout<<"Welcome to Tic Tac Toe!"<<endl;
    cout<<"1. Start Game"<<endl;
    cout<<"2. Exit"<<endl;
    int choice;
    cin>>choice;
    switch(choice)
    {
        case 1:
            start();
            break;
        case 2:
            exit(0);
            break;
        default:
            cout<<"Invalid Choice"<<endl;
            menu();
    }
}

int main()
{
    menu();
    return 0;
}