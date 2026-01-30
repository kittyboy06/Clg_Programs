#include<iostream>
#include<string.h>
#include<cstring>
using namespace std;

void lengthOfString() {
    char inp[50];
    cout << "Enter a string: ";
    cin >> inp;
    cout << "Length of string: " << strlen(inp) << endl;
}

void swapStrings() {
    char str1[50], str2[50];
    cout << "Enter first string: ";
    cin >> str1;
    cout << "Enter second string: ";
    cin >> str2;
    char temp[50];
    strcpy(temp, str1);
    strcpy(str1, str2);
    strcpy(str2, temp);
    cout << "After swapping:\n";
    cout << "First string: " << str1 << endl;
    cout << "Second string: " << str2 << endl;
}

void sizeofExample() {
    char str[50];
    cout << "Enter a string: ";
    cin >> str;
    cout << "Size of string: " << sizeof(str) << " bytes" << endl;
}

void stringConcatenation() {
    char str1[50], str2[50];
    cout << "Enter first string: ";
    cin >> str1;
    cout << "Enter second string: ";
    cin >> str2;
    strcat(str1, str2);
    cout << "Concatenated string: " << str1 << endl;
}

void stringComparison() {
    char str1[50], str2[50];
    cout << "Enter first string: ";
    cin >> str1;
    cout << "Enter second string: ";
    cin >> str2;
    if (strcmp(str1, str2) == 0) {
        cout << "Strings are equal." << endl;
    } else {
        cout << "Strings are not equal." << endl;
    }
}

void stringCopy() {
    char source[50], destination[50];
    cout << "Enter source string: ";
    cin >> source;
    strcpy(destination, source);
    cout << "Copied string: " << destination << endl;
}

void stringReverse() {
    char str[50];
    cout << "Enter a string: ";
    cin >> str;
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        swap(str[i], str[n - i - 1]);
    }
    cout << "Reversed string: " << str << endl;
}

void stringFind() {
    char str[50], ch;
    cout << "Enter a string: ";
    cin >> str;
    cout << "Enter character to find: ";
    cin >> ch;
    char *ptr = strchr(str, ch);
    if (ptr != nullptr) {
        cout << "Character found at position: " << (ptr - str) + 1 << endl;
    } else {
        cout << "Character not found." << endl;
    }
}

void stringReplace() {
    char str[50], oldChar, newChar;
    cout << "Enter a string: ";
    cin >> str;
    cout << "Enter character to replace: ";
    cin >> oldChar;
    cout << "Enter new character: ";
    cin >> newChar;
    replace(str, oldChar, newChar);
    cout << "Modified string: " << str << endl;
}

void stringSubstring() {
    char string_1[30];
    int start, length;

    cout << "Enter a string: ";
    gets(string_1);

    cout << "Enter start index and length for substring: ";
    cin >> start >> length;

    char subStr[30];

    // Get the actual length of the original string
    int str_len = strlen(string_1);

    // Validate start and length
    if (start < 0 || start >= str_len || length < 0 || start + length > str_len) {
        cout << "Invalid start or length.\n";
        return;
    }

    // Ensure we don't overflow subStr
    if (length >= sizeof(subStr))
        length = sizeof(subStr) - 1;

    strncpy(subStr, string_1 + start, length);
    subStr[length] = '\0';  // Ensure null termination

    cout << "Substring: " << subStr << endl;
}


int main()
{
    cout<<"Enter your Choice\n1. Length 11Of String\n2. Swap()\n3. Sizeof()\n4. String Concatenation\n5. String Comparison\n6. String Copy\n7. String Reverse\n8. String Find\n9. String Replace\n10. String Substring\n11. Exit"<<endl;
    int choice;
    cin>>choice;
    switch(choice)
    {
        case 1:
            lengthOfString();
            break;
        case 2:
            cout<<"Swap()"<<endl;
            swapStrings();
            cout<<"Swapped successfully!"<<endl;
            break;
        case 3:
            cout<<"Sizeof()"<<endl;
            sizeofExample();
            break;
        case 4:
            cout<<"String Concatenation"<<endl;
            stringConcatenation();
            break;
        case 5:
            cout<<"String Comparison"<<endl;
            stringComparison();
            break;
        case 6:
            cout<<"String Copy"<<endl;
            stringCopy();
            break;
        case 7:
            cout<<"String Reverse"<<endl;
            stringReverse();
            break;
        case 8:
            cout<<"String Find"<<endl;
            stringFind();
            break;
        case 9:
            cout<<"String Replace"<<endl;
            stringReplace();
            break;
        case 10:
            cout<<"String Substring"<<endl;
            stringSubstring();
            break;
        case 11:
            cout<<"Exit"<<endl;
            break;
        default:
            cout<<"Invalid Choice"<<endl;
    }
}
