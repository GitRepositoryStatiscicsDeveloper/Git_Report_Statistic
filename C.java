import java.util.Scanner;
public class C
{
    public static void main(String[] args) 
    {
        C c_obj=new C();
        c_obj.M();

    }     
    public static void M() {
        int r;
        double pi = 3.14, area;
        Scanner s = new Scanner(System.in);
        System.out.print("Please enter  radius of the circle:");
        r = s.nextInt();
        area = pi * r * r;
        System.out.println("Area of circle:"+area);
    }
}
