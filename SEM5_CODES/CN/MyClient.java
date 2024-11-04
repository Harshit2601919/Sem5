package CN;
import java.io.*;
import java.net.*;

public class MyClient {
  public static void main(String[] args) {
    try{
      Socket socket = new Socket("localhost",6666);
      DataOutputStream dataOutputStream=new DataOutputStream(socket.getOutputStream());
      dataOutputStream.writeUTF("helloo");
      dataOutputStream.flush();

      dataOutputStream.close();
      socket.close();
    }catch(Exception e){
      System.out.println("error"+e.getMessage());
      e.printStackTrace();
    }
    
  }
  
}
