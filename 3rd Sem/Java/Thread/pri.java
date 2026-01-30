package Thread;

public class pri extends Thread {
    public void run() {
        System.out.println("Thread is running.");
        System.out.println("Thread name: " + Thread.currentThread().getName());
        System.out.println("Current thread priority: " + Thread.currentThread().getPriority());
    }

    public static void main(String[] args) 
    {
        pri t1 = new pri();
        pri t2 = new pri();
        t1.setPriority(Thread.MIN_PRIORITY);
        t2.setPriority(Thread.MAX_PRIORITY);
        System.out.println("Thread priorities:"+ t1.getPriority() + " & " + t2.getPriority());
        t1.start();
        t2.start();
    }

}
