import java.rmi.Naming;

public class Server {
  public Server(){

    try {
      Matrix m = new MatrixImpl();
      Naming.rebind("//127.0.0.1:1099/MatrixService", m);
    }
    catch (Exception e) {
      System.out.println("Trouble: " + e);
    }

  }

  public static void main(String[] args) {
    new Server();
  }

}
