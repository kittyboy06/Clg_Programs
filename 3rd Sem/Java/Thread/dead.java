package Thread;

public class dead
{
    public static void main(String[] args) 
    {
        final String resource1 = "r1";
        final String resource2 = "r2";

        Thread t1 = new Thread()
        {
            public void run()
            {
                synchronized(resource1)
                {
                    System.out.println("Thread 1: Holding resource 1...");

                    try { Thread.sleep(100); } catch (Exception e) {}

                    System.out.println("Thread 1: Waiting for resource 2...");

                    synchronized(resource2)
                    {
                        System.out.println("Thread 1: Acquired resource 2!");
                    }
                }
            }
        };

        Thread t2 = new Thread()
        {
            public void run()
            {
                synchronized(resource2)
                {
                    System.out.println("Thread 2: Holding resource 2...");

                    try { Thread.sleep(100); } catch (Exception e) {}

                    System.out.println("Thread 2: Waiting for resource 1...");

                    synchronized(resource1)
                    {
                        System.out.println("Thread 2: Acquired resource 1!");
                    }
                }
            }
        };

        t1.start();
        t2.start();
    }
}
