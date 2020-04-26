package modul4_tugas_kel63;

import java.util.Scanner;

public class Modul4_Tugas_Kel63 {
    static Scanner input = new Scanner(System.in);
    public static void gambar1(){
        for (int i = 0; i <= 9; i++){
            for (int j = 0; j <= 9-i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++){
                System.out.print(i+" ");
            }
            System.out.println();
        }
    }
    public static void gambar2(){
        for (int i = 9; i > 0; i-=2){
            for (int j = 0; j <9-i/2; j++){
                System.out.print(" ");
            }
            for (int j = 0; j < i; j++){
                System.out.print("*");
            }
            System.out.print("\n");
        }
        for (int i = 2; i < 10; i+=2){
            for (int j = 0; j < 9-i/2; j++){
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++){
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
    public static void main(String[] args) {
        System.out.print("Pilihlah dari 2 gambar berikut: 1. Segtiga angka 2. Setiga bintang beradu: ");
        int pilihan;
        pilihan = input.nextInt();
        switch(pilihan){
            case 1:
                gambar1();
                break;
            case 2:
                gambar2();
                break;
            default:
                System.out.println("Tidak ada pilihan gambar lagi");
                break;
        }
    }
}
