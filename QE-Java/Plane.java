import java.time.LocalDateTime;
import java.util.*;
public class Plane {
    public List<String> passengers;
    private int maxp;
    private LocalDateTime lasttimetookof;
    private LocalDateTime lasttimelanded;
    public Plane(int maxp){
        this.maxp=maxp;
    }
    public void onboard(String name){
        passengers.add(name);
    }
    public LocalDateTime takeoff(){
        return LocalDateTime.now();
    }
    public void land(){
        lasttimelanded=LocalDateTime.now();
    }
    public LocalDateTime getLastTime(){
        return lasttimelanded;
    }
    public void getpassengers(){
        for(String n:passengers){
            System.out.println(n);
        }
    }

}
