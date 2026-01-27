import java.util.*;

public class Activity6 {
    
    public static void main(String[] args) {
        int maxp=10;
        
        Plane p=new Plane(maxp);
        p.onboard("Person1");
        p.onboard("Person2");
        p.onboard("Person3");
        p.onboard("Person4");
        p.takeoff();
        p.getpassengers();
        p.land();



        
    }

}
