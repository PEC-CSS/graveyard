T= int(input())
for i in range(0,T):
    Q = int(input()
        if Q<=36:
            print("0")
        elif Q>36:
            n = Q - 36
            if n%7 == 0:
                no_balls_reqd = n/7
                print(no_balls_reqd) 
            else:
                remainder = n%7
                x = n-remainder
                y = x/7
                no_balls_reqd = y+1
                print(int(no_balls_reqd))
                
            
        
    


