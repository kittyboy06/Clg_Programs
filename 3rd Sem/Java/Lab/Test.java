package Lab;
class Shop {
    int item;
    boolean available = false;

    synchronized void produce(int value) {
        while (available) {  // already has item
            try { wait(); } catch (Exception e) {}
        }
        item = value;
        available = true;
        System.out.println("Produced: " + value);
        notify();  // tell consumer
    }

    synchronized int consume() {
        while (!available) { // no item available
            try { wait(); } catch (Exception e) {}
        }
        available = false;
        System.out.println("Consumed: " + item);
        notify(); // tell producer
        return item;
    }
}

public class Test {
    public static void main(String[] args) {
        Shop shop = new Shop();

        Thread producer = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                shop.produce(i);
            }
        });

        Thread consumer = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                shop.consume();
            }
        });

        producer.start();
        consumer.start();
    }
}