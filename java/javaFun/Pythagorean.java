public class Pythagorean {
    public String calculateHypotenuse(int legA, int legB) {
        double Hypotenuse = Math.sqrt(Math.pow(legA, 2) + Math.pow(legB, 2));
        return "The Hypotenuse is " + Hypotenuse;
    }
}