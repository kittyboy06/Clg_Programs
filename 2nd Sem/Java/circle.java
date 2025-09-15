import static java.lang.System.out;
import java.util.Scanner;
public class circle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        out.println("Enter radius of circle: ");
        float r = sc.nextFloat();
        float area = 3.14f * r * r;
        out.println("Area of circle is: " + area);
        sc.close();
    }
}