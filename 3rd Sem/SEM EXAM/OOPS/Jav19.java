import java.util.Scanner;
class Table {
    synchronized void printTable(int n) {
        System.out.println("\nMultiplication Table of " + n + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
            try {
                Thread.sleep(400);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

// Thread 1
class ThreadOne extends Thread {
    Table t;
    int num;

    ThreadOne(Table t, int num) {
        this.t = t;
        this.num = num;
    }

    public void run() {
        t.printTable(num);
    }
}

// Thread 2
class ThreadTwo extends Thread {
    Table t;
    int num;

    ThreadTwo(Table t, int num) {
        this.t = t;
        this.num = num;
    }

    public void run() {
        t.printTable(num);
    }
}

public class Jav19 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number for multiplication table: ");
        int num1 = sc.nextInt();
        System.out.print("Enter second number for multiplication table: ");
        int num2 = sc.nextInt();

        Table obj = new Table();

        ThreadOne t1 = new ThreadOne(obj, num1);
        ThreadTwo t2 = new ThreadTwo(obj, num2);

        t1.start();
        t2.start();
        sc.close();
    }
}
