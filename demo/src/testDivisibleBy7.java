import java.util.Scanner;

public class testDivisibleBy7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        for (int j = 0; j < 3; j++) {
            // Test divisible by 7
            boolean[] boolsOut = new boolean[3];
            for (int i = 0; i < 3; i++) {
                boolsOut[i] = ExampleClass.divisibleBy7(input.nextInt());
            }

            System.out.print("{");
            for (int i = 0; i < 2; i++) {
                System.out.print(boolsOut[i] + ", ");
            }
            System.out.println(boolsOut[2] + "}");
            System.exit(0);
        }

    }

}