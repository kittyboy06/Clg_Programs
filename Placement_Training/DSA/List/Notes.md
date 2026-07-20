Linked List:
    A Linked List is a Collection of Nodes connected using references. Every node contains Data and Next reference.

 +===========+==========+
 |   Data    | Reference|
 +===========+==========+



Diff BW LinkedList/Array
 +=============+===========+
 |    Array    |Linked List|
 +=============+===========+
 |Continous    |   Random  |
 |Memory       |  Memory   |
 +=============+===========+
 |  Fixed Size |Extendabele|
 +=============+===========+

Node Structure
class Node {int data;Node next;Node(int data) {this.data = data; this.next = next;}}

Explanation:
-int data stores the value
-Node next stores the address of the next Node
-Constructor initialize data and nrxt as null

Creating Node:
Node first = new Node(10);
Node second = new Node(20);
first.next = second;

Travasel:
Node temp = head:
while(temp != null)
{
   print(temp.data); temp=temp.next;
}

Start from Head print data, move to next until NULL.
Insertion at End: Create a new node, move last node, connect last.next to new node.
