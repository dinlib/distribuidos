import java.rmi.Naming;
import java.util.Scanner;

public class Client {
  public static void main(String[] args) {


    try {
      Matrix m = (Matrix) Naming.lookup("//127.0.0.1:1099/MatrixService");

      System.out.print("Matrix Service (1 - Add | 2 - Multiplication): ");
      Scanner sc = new Scanner(System.in);
      int d = sc.nextInt();
      while(d < 1 || d > 2){
        System.out.print("Matrix Service (1 - Add | 2 - Multiplication): ");
        d = sc.nextInt();
      }
      if(d == 1){
        System.out.print("Matrix dimension: ");
        while(sc.hasNext()){
          d = sc.nextInt();
          int[][] a = m.randMatrix(d);
          int[][] b = m.randMatrix(d);
          int[][] result = m.matrixMultiplication(a, b, d);

          m.printMatrix(a, d);
          m.printMatrix(b, d);
          m.printMatrix(result, d);

          System.out.print("Matrix dimension: ");
        }
      }
      else{
        System.out.print("Matrix dimension: ");
        while(sc.hasNext()){
          d = sc.nextInt();
          int[][] a = m.randMatrix(d);
          int[][] b = m.randMatrix(d);
          int[][] result = m.matrixAdd(a, b, d);

          m.printMatrix(a, d);
          m.printMatrix(b, d);
          m.printMatrix(result, d);

          System.out.print("Matrix dimension: ");
        }
      }

    }

    catch (Exception e){
      System.out.println(e);
    }

  }
}
