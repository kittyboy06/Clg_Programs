package Lab;
import static java.lang.System.out;
import java.util.Scanner;

public class simpleinterest
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        out.println("Enter principal amount: ");
        float p = sc.nextFloat();
        out.println("Enter rate of interest: ");
        float r = sc.nextFloat();
        out.println("Enter time in years: ");
        float t = sc.nextFloat();
        float si = (p * r * t) / 100;
        out.println("Simple Interest is: " + si);
        sc.close();
    }
}