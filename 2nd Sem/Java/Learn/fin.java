package Learn;

final class Innerfin {

        final void display()
        {
            System.out.println("This is a final method in the outer class.");
        }
}

public class fin {
    public static void main(String[] args) 
    {
        final int a = 10;
        // a = 20; // This will cause a compile-time error because 'a' is final
        System.out.println("The value of a is: " + a);
    }

}
