package Thread;

public class Sle extends Thread {
    public void run() {
        try {
            for (int i = 1; i <= 5; i++) {
                System.out.println(i);
                Thread.sleep(500); // Sleep for 500 milliseconds
            }
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Sle t1 = new Sle();
        Sle t2 = new Sle();
        t1.start();
        t2.start();
    }
    
}
