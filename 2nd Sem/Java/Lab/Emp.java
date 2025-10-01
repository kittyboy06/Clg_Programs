package Lab;
import static java.lang.System.out;
import java.util.Scanner;

class Employee
{
    protected int id;
    protected String name;
    protected int age;
    protected double basicSalary;

    public void getData()
    {
        Scanner sc = new Scanner(System.in);
        out.print("Enter Employee ID: ");
        id = sc.nextInt();
        out.print("Enter Employee Name: ");
        name = sc.next();
        out.print("Enter Employee Age: ");
        age = sc.nextInt();
        out.print("Enter Employee Basic Salary: ");
        basicSalary
         = sc.nextDouble();
        sc.close();
    }

    public void displayData()
    {
        out.println("\n--- Employee Details ---");
        out.println("Employee ID: " + id);
        out.println("Employee Name: " + name);
        out.println("Employee Age: " + age);
        out.println("Employee Basic Salary: " + basicSalary);
    }

    public double calculateSalary()
    {
        return basicSalary;
    }
}

class Programmer extends Employee
{
    @Override
    public void getData()
    {
        super.getData();
    }

    @Override
    public void displayData()
    {
        super.displayData();
        
    }

    @Override
    public double calculateSalary()
    {
        return basicSalary;
    }
}

class Assistant extends Employee
{
    @Override
    public void getData()
    {
        super.getData();
    }

    @Override
    public void displayData()
    {
        super.displayData();
        
    }

    @Override
    public double calculateSalary()
    {
        return basicSalary;
    }
}

class Professor extends Employee
{
    @Override
    public void getData()
    {
        super.getData();
    }

    @Override
    public void displayData()
    {
        super.displayData();
        
    }

    @Override
    public double calculateSalary()
    {
        return basicSalary;
    }
}

public class Emp
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int choice;
        out.println("=== Employee Management System ===");
        out.println("1. Programmer");
        out.println("2. Assistant");
        out.println("3. Professor");
        out.print("Enter your choice (1-3): ");
        choice = sc.nextInt();
        Employee emp = null;
        switch (choice)
        {
            case 1:
                emp = new Programmer();
                break;
            case 2:
                emp = new Assistant();
                break;
            case 3:
                emp = new Professor();
                break;
            default:
                out.println("Invalid choice.");
                System.exit(0);
        }
        emp.getData();
        emp.displayData();
        double salary = emp.calculateSalary();
        out.println("Total Salary: " + salary);
        sc.close();
    }
}