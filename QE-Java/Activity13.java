import java.util.*;
public class Activity13 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        ArrayList<Integer> a=new ArrayList<>();
        while (sc.hasNext()) {
            if(sc.nextInt()==-1){
                break;
            }
            else{
            a.add(sc.nextInt());
            }
        }
        Random r=new Random();
        int ra=r.nextInt(a.size());
        System.out.println(a.get(ra));

    }

}
