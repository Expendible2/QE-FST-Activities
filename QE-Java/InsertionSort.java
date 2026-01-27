public class InsertionSort {
    public static void main(String[] args) {
        int arr[]={5,4,2,3,1};
        for(int i=1;i<arr.length;i++){
            int k=i;
            int j=i-1;
            while(j>=0 && arr[j]>k){
                arr[j+1]=arr[j];
                j--;
            }
            arr[j+1]=k;
        }
        for(int n:arr){
            System.out.println(n);
        }
    }
    
}
