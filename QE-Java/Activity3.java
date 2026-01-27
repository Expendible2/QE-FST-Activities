public class Activity3{
    public static void main(String[] args) {
        double earth=31557600;
        double mercury=0.2408467;
        double venus=0.61519726;
        double mars=1.8808158;
        double jupiter=11.862615;
        double saturn=84.016846;
        double uranus=84.016846;
        double neptune=164.79132;

        double sec=1000000000;

        System.out.println("Age on Earth is "+(sec/earth));
        System.out.println("Age on mercury is "+(sec/(earth*mercury)));
        System.out.println("Age on venus is "+(sec/(earth*venus)));
        System.out.println("Age on mars is "+(sec/(earth*mars)));
        System.out.println("Age on jupiter is "+(sec/(earth*jupiter)));
        System.out.println("Age on saturn is "+(sec/(earth*saturn)));
        System.out.println("Age on uranus is "+(sec/(earth*uranus)));
        System.out.println("Age on neptune is "+(sec/(earth*neptune)));
    }
}