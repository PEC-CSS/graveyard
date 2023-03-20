package cp;
import java.util.*;
class FindX {
    public static void main(String args[]) {
        Scanner I = new Scanner(System.in);
        double c = I.nextDouble();
        double x = c / 2.0; 

        while (true) {
            double func_at_x = x * x + Math.sqrt(x) - c;
            double der_of_fun_at_x = 2 * x + 1 / (2 * Math.sqrt(x));
            double xn = x - func_at_x / der_of_fun_at_x;
            if (Math.abs(xn - x) < 0.00001) {
                System.out.println(xn);
                break;
            }
            x = xn;
        }
    }
}
