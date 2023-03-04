public class cmdinput {
    public static void main(String args[]){ 
        int maxi=0; 
  
        for(int i=0;i<args.length;i++) 
        { 
            if(maxi<Integer.parseInt(args[i]))
            maxi=Integer.parseInt(args[i]);


        } 
        System.out.println("maximum value is "+maxi);  
        }  
}
