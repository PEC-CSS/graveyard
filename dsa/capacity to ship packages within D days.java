package dsa;
import java.util.*;
class ship_packs
{
    public static int shipWithinDays(int[]arr,int days,int max,int sum)
    {
        int low_l=max;
        int high_l=sum;
        int ans=0;
        if(arr.length==days)
       {
            return(max);
       }
       else
       {
            while(low_l<=high_l)
            {
                int mid_val=(int)((low_l+high_l)/2);
                if(cond(arr,mid_val,days)==true)
                {
                    ans=mid_val;
                    high_l=mid_val-1;
                }
                else
                {
                    low_l=mid_val+1;
                }
            }
            return(ans);
       }
    }
    public static boolean cond(int []arr,int mid,int days)
    {
        int k=1;
        int sum=0;
        for(int i =0;i<arr.length;i++)
        {
            sum+=arr[i];
            if(sum>mid)
            {
                k++;
                sum=arr[i];
            }
        }
        return k<=days;
    }
    
    public static void main(String args[])
    {
        Scanner I = new Scanner(System.in);
        int n,max=0,sum=0;
        System.out.println("Enter number of days");
        int days=I.nextInt();
        System.out.println("Enter length of array");
        n=I.nextInt();
        int arr[]= new int [n];
        for(int i = 0;i<=n-1;i++)
        {
            arr[i]=I.nextInt();
            System.out.println();
            sum+=arr[i];
            max=Math.max(max,arr[i]);
            
            
        }
        int ans=shipWithinDays(arr, days, max, sum);
        System.out.print(ans);
    }
}
