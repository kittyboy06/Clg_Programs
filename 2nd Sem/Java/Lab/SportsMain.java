package Lab;
interface Playable 
{
    void play(); //abstract method
}

class Football implements Playable 
{
    @Override
    public void play() {
        System.out.println("Playing football: A team sport played with a spherical ball");   
 }
}

class Volleyball implements Playable 
{
    @Override
    public void play() { 
        System.out.println("Playing Volleyball: A team sport in which two teams are separated by a net");
    }
}

class Basketball implements Playable {
    @Override
    public void play() {
        System.out.println("Playing Basketball : A game played by two teams of five players each on a rectangular court");
}
}

public class SportsMain {
    public static void main(String[] args) {
        // Create instances using the interface type
        Playable football = new Football();
        Playable volleyball = new Volleyball();
        Playable basketball = new Basketball();

        // Call the play method on each Playable object[span_5](end_span)
        football.play();
        volleyball.play();
        basketball.play();
    }
}