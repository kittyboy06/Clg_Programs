package Learn;

class newClass {
    newClass() {
        System.out.println("This is a constructor.");
    }
    void show() {
        System.out.println("This is a method.");
    }
}

public class Cons {
    public static void main(String[] args) {
        newClass oClass = new newClass();
        oClass.show();
    }
}
