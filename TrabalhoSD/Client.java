import java.rmi.Naming;
import java.util.Scanner;

public class Client {
  public static void main(String[] args) {


    try {
      Matrix m = (Matrix) Naming.lookup("//127.0.0.1:1099/MatrixService");

      System.out.println("Matrix Service");
      System.out.print("Matrix dimension: ");
      Scanner sc = new Scanner(System.in);

      while(sc.hasNext()){
        int d = sc.nextInt();
        int[][] a = m.randMatrix(d);
        int[][] b = m.randMatrix(d);
        int[][] result = m.matrixMultiplication(a, b, d);

        m.printMatrix(a, d);
        m.printMatrix(b, d);
        m.printMatrix(result, d);

        System.out.print("Matrix dimension: ");
      }

    }

    catch (Exception e){
      System.out.println(e);
    }

  }
}
