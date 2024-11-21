import java.io.File;
import java.io.IOException;

//window stuff and all that
import java.awt.*;
 import java.awt.event.*;
//racism 
import javax.swing.*;
 import javax.swing.event.*;

//TODO: make it play a FUCKING SOUND
//TODO: make the trea, principle window -> secondary *temporary* window -> window with sound

public class are_you_an_lobster extends JPanel {
    //construct components
    How = new JTextField (1);
    jcomp2 = new JLabel("welcome to the lobster test");
    jcomp3 = new JLabel("Start");
    
    jcomp4.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            JFrame frame = new JFrame("My Pannel");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.getContentPane().add (new are_you_an_lobster());
            frame.pack();
            frame.setVisible(true);
        }
    });


    //add components
    add (How);    
    add (jcomp2);
    add (jcomp3);    

    public static void main (String[] args) {
        JFrame frame = new JFrame("My Panel");
        frame.serDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add (new are_you_an_lobster());
        frame.pack();
        frame.setVisible(true);
    }
}