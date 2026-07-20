import java.util.*;

public class Linked_List_InsertAtEnd {
    
    public static class Node
    {
        int data;
        Node next;
        Node(int data)
        {
            this.data = data;
            this.next = null;
        }
    }
    
    static Node InsertAtEnd(Node Head,int data)
    {
        Node insert = new Node(data);
        Node temp = Head;
        if(temp == null)
        {
            Head = insert;
        }
        else
        {
            while(temp.next != null)
            {
                temp = temp.next;
            }
        
            temp.next = insert;
        }
        
        return Head;
    }
    static void Display(Node head) 
    {
        while (head != null) 
        {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Node head = null;
        for(int i = 0; i < N; i++)
        {
            int data = sc.nextInt();
            head = InsertAtEnd(head, data);
        }
        Display(head);
    }
}