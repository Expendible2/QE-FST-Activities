public class Bicycle implements Bicycleparts, Bicycleoperations{
    public int currentspeed;
    public int gears;
    public Bicycle(){
        gears=3;
        currentspeed=85;
    }
    @Override
    public void applybrake(int seconds){
        currentspeed=currentspeed-seconds;
    }
    @Override
    public void speedup(int seconds){
        currentspeed=currentspeed+seconds;
    }
    public void desc(){
        System.out.println("gears "+gears+"\nspeed "+currentspeed);
    }
}
