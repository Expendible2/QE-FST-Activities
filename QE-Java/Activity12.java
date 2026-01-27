public class Activity12 {

    public static void main(String[] args) {
        Addable ad1=(int a, int b)->
            {return (a+b);};
        Addable ad2=(a,b)->(a+b);

        int num1=ad1.add(1, 2);
        int num2=ad2.add(5, 6);
        System.out.println(num1+" "+ num2);


        
    }

}
