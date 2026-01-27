public class MountainBike extends Bicycle{
    private int seatHight;
    public void setHeight(int val){
        seatHight=val;
    }
    @Override
    public void desc(){
        System.out.println("gears "+gears+" speed "+currentspeed+" seatheight "+seatHight);
    }
    public static void main(String[] args) {
        MountainBike mb=new MountainBike();
        mb.desc();
        mb.speedup(10);
        mb.applybrake(5);
        mb.setHeight(10);
        mb.desc();
    }
}
