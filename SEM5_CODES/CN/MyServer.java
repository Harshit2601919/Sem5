package CN;
import java.io.*;
import java.net.*;
public class MyServer {
  public static void main(String[] args) {
    try{
      ServerSocket serverSocket=new ServerSocket(6666);
      System.out.println("server is lisetining to port 6666");

      Socket socket=serverSocket.accept();
      System.out.println("connecteddddddd");


      DataInputStream dataInputStream=new DataInputStream(socket.getInputStream());
      String message =dataInputStream.readUTF();
      System.out.println("message from client is "+message);

      dataInputStream.close();
      serverSocket.close();
      socket.close();
    }catch(Exception e){
      System.out.println("error"+e.getMessage());
      e.printStackTrace();
    }
  }
  
}
