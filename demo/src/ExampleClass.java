public class ExampleClass {
  public static double[] squareEachNumber(double[] input) {
    double[] returnArr = new double[input.length];
    for (int i = 0; i < input.length; i++) {
      returnArr[i] = input[i] * input[i];
    }
    return returnArr;
  }

  public static boolean divisibleBy7(int num) {
    return num % 7 == 0;
  }
}
