import java.util.*;

class Employee {
    String empName, empId, address, mailId, mobileNo;

    Employee(String empName, String empId, String address, String mailId, String mobileNo) {
        this.empName = empName;
        this.empId = empId;
        this.address = address;
        this.mailId = mailId;
        this.mobileNo = mobileNo;
    }

    void display() {
        System.out.println("\nEMPLOYEE DETAILS");
        System.out.println("Name       : " + empName);
        System.out.println("ID         : " + empId);
        System.out.println("Address    : " + address);
        System.out.println("Mail ID    : " + mailId);
        System.out.println("Mobile No  : " + mobileNo);
    }
}

class Programmer extends Employee {
    double bp;

    Programmer(String empName, String empId, String address, String mailId, String mobileNo, double bp) {
        super(empName, empId, address, mailId, mobileNo);
        this.bp = bp;
    }

    void generatePayslip() {
        double da = 0.97 * bp;
        double hra = 0.10 * bp;
        double pf = 0.12 * bp;
        double club = 0.001 * bp;
        double gross = bp + da + hra;
        double net = gross - pf - club;

        display();
        System.out.println("\n--- PROGRAMMER PAYSLIP ---");
        System.out.println("Basic Pay          : " + bp);
        System.out.println("DA (97%)           : " + da);
        System.out.println("HRA (10%)          : " + hra);
        System.out.println("PF (12%)           : " + pf);
        System.out.println("Staff Club (0.1%)  : " + club);
        System.out.println("Gross Salary       : " + gross);
        System.out.println("Net Salary         : " + net);
    }
}

class AssistantProfessor extends Programmer {
    AssistantProfessor(String empName, String empId, String address, String mailId, String mobileNo, double bp) {
        super(empName, empId, address, mailId, mobileNo, bp);
    }

    void generatePayslip() {
        System.out.println("\n--- ASSISTANT PROFESSOR PAYSLIP ---");
        super.generatePayslip();
    }
}

class AssociateProfessor extends Programmer {
    AssociateProfessor(String empName, String empId, String address, String mailId, String mobileNo, double bp) {
        super(empName, empId, address, mailId, mobileNo, bp);
    }

    void generatePayslip() {
        System.out.println("\n--- ASSOCIATE PROFESSOR PAYSLIP ---");
        super.generatePayslip();
    }
}

class Professor extends Programmer {
    Professor(String empName, String empId, String address, String mailId, String mobileNo, double bp) {
        super(empName, empId, address, mailId, mobileNo, bp);
    }

    void generatePayslip() {
        System.out.println("\n--- PROFESSOR PAYSLIP ---");
        super.generatePayslip();
    }
}

public class Jav14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n===== EMPLOYEE PAYSLIP MENU =====");
            System.out.println("1. Programmer");
            System.out.println("2. Assistant Professor");
            System.out.println("3. Associate Professor");
            System.out.println("4. Professor");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();  // consume newline

            if (choice >= 1 && choice <= 4) {
                System.out.print("Enter Employee Name: ");
                String name = sc.nextLine();
                System.out.print("Enter Employee ID: ");
                String id = sc.nextLine();
                System.out.print("Enter Address: ");
                String address = sc.nextLine();
                System.out.print("Enter Mail ID: ");
                String mail = sc.nextLine();
                System.out.print("Enter Mobile No: ");
                String mobile = sc.nextLine();
                System.out.print("Enter Basic Pay: ");
                double bp = sc.nextDouble();

                switch (choice) {
                    case 1:
                        Programmer p = new Programmer(name, id, address, mail, mobile, bp);
                        p.generatePayslip();
                        break;
                    case 2:
                        AssistantProfessor ap = new AssistantProfessor(name, id, address, mail, mobile, bp);
                        ap.generatePayslip();
                        break;
                    case 3:
                        AssociateProfessor asp = new AssociateProfessor(name, id, address, mail, mobile, bp);
                        asp.generatePayslip();
                        break;
                    case 4:
                        Professor prof = new Professor(name, id, address, mail, mobile, bp);
                        prof.generatePayslip();
                        break;
                }
            } else if (choice != 5) {
                System.out.println("Invalid choice! Please try again.");
            }

        } while (choice != 5);

        System.out.println("Exiting... Thank you!");
        sc.close();
    }
}
