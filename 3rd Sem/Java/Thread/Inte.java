package Thread;

public class Inte implements Runnable {
    public void run()
    {
        System.out.println("Thread is running.");
    }
    public static void main(String[] args)
    {
        Inte obj = new Inte();
        Thread t1 = new Thread(obj);
        t1.start();
    }
}
