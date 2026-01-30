public class Jav15 extends Thread {
    public void run() {
        System.out.println("Thread is running.");
        System.out.println("Thread name: " + Thread.currentThread().getName());
        System.out.println("Current thread priority: " + Thread.currentThread().getPriority());
    }

    public static void main(String[] args) 
    {
        Jav15 t1 = new Jav15();
        Jav15 t2 = new Jav15();
        t1.setPriority(Thread.MIN_PRIORITY);
        t2.setPriority(Thread.MAX_PRIORITY);
        System.out.println("Thread priorities:"+ t1.getPriority() + " & " + t2.getPriority());
        t1.start();
        t2.start();
    }

}
