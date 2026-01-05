package Demo.TicTacToe;
import static java.lang.System.*;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class XOMain 
{
    public static void main(String[] args) {
        JFrame frame = new JFrame("Tic Tac Toe");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setVisible(true);
        JLabel label = new JLabel("Welcome to Tic Tac Toe!");
        frame.getContentPane().add(label);
        
    }
}
