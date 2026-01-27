import java.util.HashMap;

public class Activity11 {
    public static void main(String[] args) {
        HashMap<Integer, String> a=new HashMap<>();
        a.put(1, "Person1");
        a.put(2, "Person2");
        a.put(3, "Person3");
        a.put(4, "Person4");
        a.put(3, "Person3");

        a.remove(1);
        System.out.println(a.containsValue("Person2"));
        System.out.println(a.size());

    }

}
