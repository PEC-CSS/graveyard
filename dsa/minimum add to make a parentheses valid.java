package dsa;
import java.util.*;
class grave
{
    public static void main(String args[])
    {
            Scanner I = new Scanner (System.in);
            System.out.println("Enter a string");
            String s = I.nextLine(); 
            Stack<Character>st=new Stack<>();
            char ch;
            for(int i =0 ; i<=s.length()-1;i++)
            {
                ch=s.charAt(i);
                if(ch=='(')
                {
                    st.push(ch);
                }
                else
                {
                    if(st.size()>0 && st.peek()=='(')
                    {
                        st.pop();
                    }
                    else
                    {
                        st.push(ch);
                    }
                }
            }
            System.out.println("Number of extra parenthesis ="+st.size());
            I.close();
    }
}
        
    
