import java.util.ArrayList;
import java.util.List;

public class Activity9 {
    public static void main(String[] args) {
        
    
    ArrayList<String> al =new ArrayList<>();
    al.add("Person1");
    al.add("Person2");
    al.add("Person3");
    al.add("Person4");
    al.add("Person5");
    
    for(String n:al){
        System.out.println(n);
    }
    al.get(3);
    if(al.contains("Person1")){
        System.out.println("Present");
    }
    System.out.println(al.size());
    al.remove("Person1");
    System.out.println(al.size());
    }

}
