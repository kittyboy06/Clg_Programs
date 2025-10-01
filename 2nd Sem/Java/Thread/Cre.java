package Thread;

public class Cre extends Thread {
    public void run() {
        System.out.println("Thread is running.");
    }

    public static void main(String[] args) {
        Cre t1 = new Cre();
        t1.start();
    }
    
}
