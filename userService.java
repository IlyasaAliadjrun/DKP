/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modul5_kel63;

/**
 *
 * @author VivoBook S430F
 */
class userService {
    private String[][] data = new String[2][3];
    private String[][] histories = new String[2][4];
    private String email, password, roles,b,c,d= "";
    
    //ini namanya constructor yang akan dijalankan setiap class diinisialisasikan
    public userService(String emails, String passwords)
    {
        email = emails;
        password = passwords;
        
        
        String[][] data = 
        { 
            {"fariskelompok63@gmail.com", "12345", "supedAdmin"},
            {"ilyasakelompok63@gmail.com", "12345", "user"} 
        };
        String [][] histories =
        {
            {"fariskelompok63@gmail.com", "Fisika Dasar", "Dasar Komputer dan Pemograman", "26-04-2020"},
            {"ilyasakelompok63@gmail.com", "Fisika Dasar", "Dasar Komputer dan Pemograman", "26-04-2020"}
    };
        this.data = data;
        this.histories = histories;
    }
    
    private boolean checkCredential()
    {
        for(int i = 0; i < data.length ; i++ )
        {
            for(int j = 0; j < histories.length ; j++ )
        {
            if(data[i][0].equals(email))
            {
                if(data[i][1].equals(password))
                {
                    roles = data[i][2];
                    {
                        b = histories[j][1];
                        {
                             c =histories[j][2];
                             {
                                  d = histories [j][3];
                             }
                        }
                    
                    return true;
                }
            }
        
            }
        }
       }
        
        return false;
    }
    
    public void login()
    {
        boolean status = checkCredential();
        if(status == true)
        {
            System.out.println("\nWelcome " + roles);
            System.out.println("Logged it as user email " + email);
            System.out.println(email + " meminjam buku : ");
            System.out.println(b);
            System.out.println(c);
            System.out.println("Tanggal Pinjaman " + d);
        }
        else
        {
            System.out.println("\nInvalid Login ");
        }
    }
}
