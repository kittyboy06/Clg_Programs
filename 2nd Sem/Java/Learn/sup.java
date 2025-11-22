package Learn;

class Animal
{
    Animal()
    {
        System.out.println("Animal is created");
    }

    public String color = "Black";
    void eat()
    {
        System.out.println("Eating...");
    }
}

class Dog extends Animal
{
    Dog()
    {
        super();
        System.out.println("Dog is created");
    }

    public String color = "Brown";
    void bark()
    {
        System.out.println("Barking...");
    }
    void eat()
    {
        System.out.println("Eating bread...");
    }
    void work()
    {
        super.eat();
        bark();
    }
    void showColor()
    {
        System.out.println(super.color);
    }
}

public class sup {
    public static void main(String[] args)
    {
        Dog dog = new Dog();
        dog.work();
        System.out.println(dog.color);
        //System.out.println(dog.super.color);
        dog.showColor();
    }
}
