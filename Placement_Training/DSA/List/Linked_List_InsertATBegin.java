import java.util.*;

public class Linked_List_InsertATBegin 
{
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
    
    static Node InsertAtBegining(Node head,int data)
    {
        Node newNode = new Node(data);
        if(head == null)
        {
            head = newNode;
        }
        else
        {
            newNode.next = head;
            head = newNode;
        }
        return head;
    }
    
    static void Display(Node head)
    {
        while(head != null)
        {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }
    
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Node head = null;
        for(int i = 0; i<N ; i++)
        {
            int data = sc.nextInt();
            head = InsertAtBegining(head, data);
        }
        Display(head);
        sc.close();
    }
}
