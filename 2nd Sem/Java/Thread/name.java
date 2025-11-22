package Thread;
import static java.lang.System.out;

public class name extends Thread {
    public void run() {
        out.println("Thread is running.");
    }

    public static void main(String[] args) {
        name t1 = new name();
        name t2 = new name();
        out.println("Thread names:"+ t1.getName() + " & " + t2.getName());
        t1.start();
        t2.start();
        t1.setName("1st");
        t2.setName("2nd");
        out.println("Thread names:"+ t1.getName() + " & " + t2.getName());
    }
    
}
