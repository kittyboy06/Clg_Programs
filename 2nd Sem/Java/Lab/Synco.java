package Lab;
class Table {
    // The 'synchronized' keyword ensures that only one thread can execute this method at a time.
    synchronized void printTable() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Value: " + i);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

class Thread1 extends Thread {
    Table table;

    Thread1 (Table table) {
        this.table = table;
    }

    public void run() {
        table.printTable();
        System.out.println(); // Added a blank line for output separation
    }
}

class Thread2 extends Thread {
    Table table;

    Thread2 (Table table) {
        this.table = table;
    }

    public void run() {
        table.printTable();
    }
}

public class Synco {
    public static void main (String[] args) {
        Table table = new Table();

        Thread1 thread1 = new Thread1 (table);
        Thread2 thread2 = new Thread2 (table);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            System.out.println(e);
        }

        System.out.println("table Printed");
    }
}
