import java.util.Random;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class MatrixImpl extends java.rmi.server.UnicastRemoteObject implements Matrix {

  public MatrixImpl() throws java.rmi.RemoteException {
      super();
  }

  public int[][] randMatrix(int size) throws java.rmi.RemoteException {
    int[][] m = new int[size][size];
    try{
      System.out.println("Using MatrixService to request MatrixService1 a randMatrix");
      MatrixRemote m1 = (MatrixRemote) Naming.lookup("rmi://127.0.0.1:1099/MatrixService1");
      m = m1.randMatrixRemote(size);
    }
    catch(Exception e){
      e.printStackTrace();
    }
    return m;
  }

  public void printMatrix(int[][] m, int size) throws java.rmi.RemoteException {
    try{
      System.out.println("Using MatrixService to request MatrixService1 a printMatrix");
      MatrixRemote m1 = (MatrixRemote) Naming.lookup("rmi://127.0.0.1:1099/MatrixService1");
      m1.printMatrixRemote(m, size);
    }
    catch(Exception e){
      e.printStackTrace();
    }
  }

  public int[][] matrixMultiplication(int[][] a, int[][] b, int size) throws java.rmi.RemoteException {
    int[][] result = new int[size][size];
    try{
      System.out.println("Using MatrixService to request MatrixService1 a matrixMultiplication");
      MatrixRemote m1 = (MatrixRemote) Naming.lookup("rmi://127.0.0.1:1099/MatrixService1");
      result = m1.matrixMultiplicationRemote(a, b, size);
    }
    catch(Exception e){
      e.printStackTrace();
    }
    return result;
  }

  public int[][] matrixAdd(int[][] a, int[][] b, int size) throws java.rmi.RemoteException {
    int[][] result = new int[size][size];
    try{
      System.out.println("Using MatrixService to request MatrixService1 a matrixAdd");
      MatrixRemote m1 = (MatrixRemote) Naming.lookup("rmi://127.0.0.1:1099/MatrixService1");
      result = m1.matrixAddRemote(a, b, size);
    }
    catch(Exception e){
      e.printStackTrace();
    }
    return result;
  }
}
