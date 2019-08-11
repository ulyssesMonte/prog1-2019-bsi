import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("digite um número ");
    int x = input.nextInt();
    if ((x % 2)==0){
      System.out.println("PAR ");
    }
    else{
      System.out.println("IMPAR ");
    }
  }
}