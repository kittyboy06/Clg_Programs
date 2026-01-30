package Learn;

class newClass_Para
{
    newClass_Para(int x) 
    {
        System.out.println("This is a parameterized constructor with value: " + x);
    }
    void show() 
    {
        System.out.println("This is a method.");
    }
}

public class Para_Cons {
    public static void main(String[] args) {
        newClass_Para obj = new newClass_Para(5);
        obj.show();
    }
}
