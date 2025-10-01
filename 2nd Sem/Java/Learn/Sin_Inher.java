package Learn;

class Vehicle
{
    void run()
    {
        System.out.println("Vehicle is running");
    }
}

class Bike extends Vehicle
{
    void run()
    {
        System.out.println("Bike is running safely");
    }
}

public class Sin_Inher {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        v.run();

        Bike b = new Bike();
        b.run();
    }
}
