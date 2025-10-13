package Lab;

class Table
{
    void printTable()
    {
        for(int i=1;i<=5;i++)
        {
            System.out.println("Value: "+i);
            try
            {
                Thread.sleep(100);
            }
            catch (InterruptedException e)
            {
                System.out.println(e);
            }
        }
    }
}

class Thread1 extends Thread
{
    Table t;
    Thread1(Table t)
    {
        this.t=t;
    }
    public void run()
    {
        t.printTable();
    }
}

class Thread2 extends Thread
{
    Table t;
    Thread2(Table t)
    {
        this.t=t;
    }
    public void run()
    {
        t.printTable();
    }
}

public class WSynco {
    public static void main(String[] args) {
        Table obj = new Table();
        Thread1 t1 = new Thread1(obj);
        Thread2 t2 = new Thread2(obj);
        t1.start();
        t2.start();
        try
        {
            t1.join();
            t2.join();
        }
        catch (InterruptedException e)
        {
            System.out.println(e);
        }
        System.out.println("Tables printed");
    }
}
