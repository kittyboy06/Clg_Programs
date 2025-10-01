package Thread;

public class Dae extends Thread {
    public void run() {
        if(Thread.currentThread().isDaemon()) {
            System.out.println("Daemon thread is running.");
        } else {
            System.out.println("User thread is running.");
        }
    }

    public static void main(String[] args) {
        Dae t1 = new Dae();
        Dae t2 = new Dae();
        Dae t3 = new Dae();
        t1.setDaemon(true);
        t1.start();
        t2.start();
        t3.start();
    }
    
}
