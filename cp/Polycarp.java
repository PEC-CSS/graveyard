package cp;

import java.util.Arrays;
import java.util.Scanner;

public class Polycarp {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int contest[] = new int[n];
        for(int i = 0; i < n; i++) {
            contest[i] = sc.nextInt();
        }
        Arrays.sort(contest);
        int day = 1;
        for(int i = 0; i < contest.length; i++) {
            if(day <= contest[i]) {
                day++;
            }
        }
        System.out.println(day - 1);
        sc.close();
    }
}
