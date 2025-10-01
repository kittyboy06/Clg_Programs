package Learn;

class Add
{
    Add(int a, int b)
    {
        System.out.println("Sum: " + (a + b));
    }

    Add(int a, int b, int c)
    {
        System.out.println("Sum: " + (a + b + c));
    }

    Add(double a, double b)
    {
        System.out.println("Sum: " + (a + b));
    }
}
public class Over 
{
    public void Add(int a, int b)
    {
        System.out.println("Sum: " + (a + b));
    }

    public static void main(String[] args)
    {
        Add obj1 = new Add(5, 10);
        Add obj2 = new Add(5, 10, 15);
        Add obj3 = new Add(5.5, 10.5);
    }
}
