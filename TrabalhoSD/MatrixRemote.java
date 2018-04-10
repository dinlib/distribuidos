import java.rmi.RemoteException;

public interface MatrixRemote extends java.rmi.Remote {

  public int[][] randMatrixRemote(int size) throws java.rmi.RemoteException;
  public void printMatrixRemote(int[][] m, int size) throws java.rmi.RemoteException;
  public int[][] matrixMultiplicationRemote(int[][] a, int[][] b, int size) throws java.rmi.RemoteException;
  public int[][] matrixAddRemote(int[][] a, int[][] b, int size) throws java.rmi.RemoteException;

}
