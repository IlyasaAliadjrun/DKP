package modul5_kel63;
import java.util.Scanner;


public class Modul5_kel63 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        String email, password;
        
        Scanner input = new Scanner(System.in);
        System.out.print("Email : ");
        email = input.nextLine();
        System.out.print("Password : ");
        password = input.nextLine();
        
        userService satu = new userService( email, password);
        satu.login();
    }
    
}
