package Learn;

class Example {
    int x;

    Example(int x) {
        this.x = x; // 'this' refers to the current object's instance variable
    }

    void display() {
        System.out.println("Value of x: " + this.x); // 'this' is used to refer to the current object's variable
    }

    void show() {
        this.display(); // 'this' is used to call the current object's method
    }

    Example()
    {
        this(10); // 'this' is used to call another constructor in the same class
        System.out.println("Default constructor called");
    }
}

public class thiskey {
    public static void main(String[] args) {
        Example obj = new Example(5);
        obj.display();
    }
}
