public class Test {
    public static void main(String[] args) {
        int arr[]={10,77,10,54,-11,10};
        int s=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==10){
                s+=arr[i];
            }
        }
        if (s==30){
            System.out.println("The sum of 10's in the array is "+s);
        }
        else{
            System.out.println("The sum of array is not equal to 30");
        }
    }   
}
