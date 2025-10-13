package Geo;

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle(5);
        Rectangle rectangle = new Rectangle(4, 6);

        System.out.println("Circle:");
        System.out.println("Radius: " + circle.radius);
        System.out.println("Area: " + circle.area());
        System.out.println("Circumference: " + circle.circumference());

        System.out.println("\nRectangle:");
        System.out.println("Length: " + rectangle.length);
        System.out.println("Breadth: " + rectangle.breadth);
        System.out.println("Area: " + rectangle.area());
        System.out.println("Perimeter: " + rectangle.perimeter());
    }
}
