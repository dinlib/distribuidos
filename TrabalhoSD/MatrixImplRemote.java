import java.util.Random;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class MatrixImplRemote extends java.rmi.server.UnicastRemoteObject implements MatrixRemote {

  public MatrixImplRemote() throws java.rmi.RemoteException {
      super();
  }

  public int[][] randMatrixRemote(int size) throws java.rmi.RemoteException {
    int[][] m = new int[size][size];
    Random rand = new Random();
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        m[i][j] = rand.nextInt(10);
      }
    }
    return m;
  }

  public void printMatrixRemote(int[][] m, int size) throws java.rmi.RemoteException {
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        System.out.print(m[i][j] + " ");
      }
      System.out.println();
    }
    System.out.println();
  }

  public int[][] matrixMultiplicationRemote(int[][] a, int[][] b, int size) throws java.rmi.RemoteException {
    int[][] result = new int[size][size];
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        for (int k = 0; k < size; k++){
          result[i][j] += a[i][k] * b[k][j];
        }
      }
    }
    return result;
  }
}
