import java.util.Scanner;
import static java.lang.System.out;

public class Jav12
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        out.print("Enter the First Number: ");
        int a = sc.nextInt();
        out.print("Enter the Second Number: ");
        int b = sc.nextInt();
        int sum = a + b;
        int diff = a - b;
        int prod = a * b;
        int quot = a / b;
        int rem = a % b;
        out.println("Sum: " + sum);
        out.println("Difference: " + diff);
        out.println("Product: " + prod);
        out.println("Quotient: " + quot);
        out.println("Remainder: " + rem);
        sc.close();
    }
}