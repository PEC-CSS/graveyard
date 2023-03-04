package cp;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Scanner;

public class PECFootballTour {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        sc.nextLine();
        HashMap<String, Integer> map = new HashMap<>();
        for(int i = 0; i < total; i++) {
            String team = sc.nextLine();
            if(map.containsKey(team)) {
                map.put(team, map.get(team) + 1);
            } else {
                map.put(team, 1);
            }
        }
        String winningTeam = "";
        int maxScore = 0;
        for(Entry<String, Integer> entry : map.entrySet()) {
            if(entry.getValue() > maxScore) {
                winningTeam = entry.getKey();
                maxScore = entry.getValue();
            }
        }
        System.out.println(winningTeam);
        sc.close();
    }
}
