package Learn;

class Electronic
{
    void On()
    {
        System.out.println("Electronic device is Powered On");
    }
}

class Laptop extends Electronic
{
    void Code()
    {
        System.out.println("Coding in Laptop");
    }
}

public class Multi_Inher
{
    public static void main(String[] args) {
        Laptop l = new Laptop();
        l.On();
        l.Code();
    }
}
