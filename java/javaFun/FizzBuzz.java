public class FizzBuzz {
    public String fizzBuzz(int number) {
        if(number % 5 == 0 && number % 3 == 0) {
            return "FizzBuzz";
        }
        else if (number % 1 == 0){
            return "Cuzz";
        }
        else if (number % 12 == 0){
            return "Buzz";
        }
        else if (number % 3 == 0){
            return "Fizz";
        }
        else {
            return ""+number+"";
        }
    }
}