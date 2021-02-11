import java.util.Scanner;

public class testSquareEachNumber {
    public static void main(String[] args) {
        // Scanner for inputs
        Scanner input = new Scanner(System.in);
        for (int j = 0; j < 3; j++) {
            // Test Square Each Number
            double[] numsIn = new double[3]; // Take in 3 numbers
            for (int i = 0; i < 3; i++) {
                numsIn[i] = input.nextDouble();
            }

            double[] numsOut = ExampleClass.squareEachNumber(numsIn);
            System.out.print("{");
            for (int i = 0; i < 2; i++) {
                System.out.print(numsOut[i] + ", ");
            }
            System.out.println(numsOut[2] + "}");
            System.exit(0);
        }
    }
}
