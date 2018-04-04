import java.rmi.Naming;

public class Client {
  public static void main(String[] args) {

    try {
      Matrix m = (Matrix) Naming.lookup("//127.0.0.1:1099/MatrixService");
      Calculator c = (Calculator) Naming.lookup("//127.0.0.1:1099/CalculatorService");

      System.out.println("Calculator Service");
      System.out.println(c.sub(10, 2));
      System.out.println(c.add(10, 2));
      System.out.println(c.mul(10, 2));
      System.out.println(c.div(10, 2));

      System.out.println("Matrix Service");
      int[][] a = m.randMatrix(4);
      int[][] b = m.randMatrix(4);
      int[][] result = m.matrixMultiplication(a, b, 4);

      m.printMatrix(a, 4);
      m.printMatrix(b, 4);
      m.printMatrix(result, 4);
    }

    catch (Exception e){
      System.out.println(e);
    }

  }
}
