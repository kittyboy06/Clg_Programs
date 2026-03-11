class Sample {
    int value;

    Sample(int value) {
        this.value = value;
    }

    Sample getInstance() {
        System.out.println("Returning the current class instance...");
        return this;
    }

    void display() {
        System.out.println("Value: " + value);
        System.out.println("Current Object Reference: " + this);
    }
}

public class Jav16 {
    public static void main(String[] args) {
        Sample obj = new Sample(100);
        obj.display();

        Sample returnedObj = obj.getInstance();

        System.out.println("Returned Object Reference: " + returnedObj);

        if (obj == returnedObj)
            System.out.println("Both references refer to the same instance!");
    }
}
