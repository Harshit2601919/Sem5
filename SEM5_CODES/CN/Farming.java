package CN;

import java.util.*;

public class Farming{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    boolean x= true;
    System.out.println("enter the string");
    String input =sc.nextLine();
    System.out.println("menu \n 1.character count \n2.byte stuffing \n3.bit stuffing \n4.physical data \n5.exit");
    while(x){
      System.out.println("enter you choice");
      int option=sc.nextInt();

      switch(option){
        case 1:
          System.out.println(input.length()+input);
          break;
        case 2:
          StringBuilder bytestuffing=new StringBuilder();
          bytestuffing.append("F");
          for(int i=0;i<input.length();i++){
            if(input.charAt(i)=='F'){
              bytestuffing.append("E");
            }
            if(input.charAt(i)=='E'){
              bytestuffing.append("E");
            }
            bytestuffing.append(input.charAt(i));

          }
          bytestuffing.append("F");
          System.out.println(bytestuffing);
          break;
        case 3:
          StringBuilder bitstuffing =new StringBuilder();
          int count=0;
          for(int i=0;i<input.length();i++){
            bitstuffing.append(input.charAt(i));
            if(input.charAt(i)==1){
              count++;
            }
            else{
              count=0;
            }
            if(count==5){
              bitstuffing.append("0");
            }
          }
          System.out.println(bitstuffing);
          break;
        case 4 :
          System.out.println(input+01);
          break;
        case 5:
          x=false;
          break;
        default:
        System.out.println("please enter the valid optionnn");
        break;
      }




  }
  sc.close();
}
}