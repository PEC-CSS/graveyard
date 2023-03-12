package misc;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.util.Scanner;

public class issue134 {
    
    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);
        boolean exit = false;
    
        while (!exit) {
            System.out.println("Select an option:");
            System.out.println("1. date - Shows current date");
            System.out.println("2. python - Execute a python file");
            System.out.println("3. list - List current directory");
            System.out.println("4. color - Changes text color");
            System.out.println("5. ipc - Returns IP and HOSTNAME");
            System.out.println("6. spec - System specifications");
            System.out.println("7. gendir - Generate a new directory");
            System.out.println("8. exit - Exits this program");
    
            int option = scanner.nextInt();
            scanner.nextLine(); 
    
            switch (option) {
                case 1:
                    showDate();
                    break;
                case 2:
                    executePython();
                    break;
                case 3:
                    listDirectory();
                    break;
                case 4:
                    changeTextColor();
                    break;
                case 5:
                    showIPAndHostname();
                    break;
                case 6:
                    showSystemSpecs();
                    break;
                case 7:
                    generateDirectory();
                    break;
                case 8:
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid option!");
            }
        }
    
        scanner.close();
        System.out.println("Exiting program...");
    }
    
    private static void showDate() {
        System.out.println("Current date: " + new java.util.Date());
    }
    
    private static void executePython() throws IOException {
        System.out.println("Enter the path of the python file:");
        String path = new BufferedReader(new InputStreamReader(System.in)).readLine();
    
        ProcessBuilder pb = new ProcessBuilder("python", path);
        Process p = pb.start();
    
        try {
            p.waitFor();
            System.out.println("Python script executed successfully!");
        } catch (InterruptedException e) {
            System.out.println("Failed to execute python script!");
            e.printStackTrace();
        }
    }
    
    private static void listDirectory() {
        File dir = new File(".");
        File[] files = dir.listFiles();
    
        for (File file : files) {
            if (file.isDirectory()) {
                System.out.println("[" + file.getName() + "]");
            } else {
                System.out.println(file.getName());
            }
        }
    }
    
    private static void changeTextColor() {
        System.out.println("Enter the color code (0-7):");
        int colorCode = new Scanner(System.in).nextInt();
    
        System.out.println("\u001B[3" + colorCode + "mText color changed!");
    }
    
    private static void showIPAndHostname() throws IOException {
        InetAddress inetAddress = InetAddress.getLocalHost();
        String ip = inetAddress.getHostAddress();
        String hostname = inetAddress.getHostName();
    
        System.out.println("IP address: " + ip);
        System.out.println("Hostname: " + hostname);
    }
    
    private static void showSystemSpecs() {
        System.out.println("OS name: " + System.getProperty("os.name"));
        System.out.println("OS version: " + System.getProperty("os.version"));
        System.out.println("Java version: " + System.getProperty("java.version"));
        
    }
    
    private static void generateDirectory() throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the directory name:");
        String dirName = scanner.nextLine();
    
        File dir = new File(dirName);
    
        if (dir.mkdir()) {
            System.out.println("Directory created successfully!");
        } else {
            System.out.println("Failed to create directory!");
        }
    }
    
    }
    
