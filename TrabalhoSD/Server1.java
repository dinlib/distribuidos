import java.rmi.Naming;

public class Server1 {
  public Server1(){

    try {
      MatrixRemote m = new MatrixImplRemote();
      Naming.rebind("//127.0.0.1:1099/MatrixService1", m);
    }
    catch (Exception e) {
      System.out.println("Trouble: " + e);
    }

  }

  public static void main(String[] args) {
    new Server1();
  }

}
