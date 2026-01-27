public class customexception{
    public static class myexception extends Exception{
    private String message;
    public myexception(String msg){
        this.message=msg;
    }
    @Override
    public String getMessage(){
        return message;
    }
    }
    public static void exceptiontest(String message) throws myexception{
        if(message==null){
            throw new myexception("String is null");
        }
        else{
            System.out.println(message);
        }
    }


    public static void main(String[] args) {
        try{
            exceptiontest("String is not null");
            exceptiontest(null);
        }
        catch(myexception e){
            System.out.println(e.getMessage());

        }
    }
}


