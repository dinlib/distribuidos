import java.rmi.RemoteException;

public interface Matrix extends java.rmi.Remote {

  public int[][] randMatrix(int size) throws java.rmi.RemoteException;
  public void printMatrix(int[][] m, int size) throws java.rmi.RemoteException;
  public int[][] matrixMultiplication(int[][] a, int[][] b, int size) throws java.rmi.RemoteException;
  public int[][] matrixAdd(int[][] a, int[][] b, int size) throws java.rmi.RemoteException;

}
