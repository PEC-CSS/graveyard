#include <iostream>
using namespace std;

int ways(int n){
    if (n==0){
        return 1;
    }
    else if (n==1){
        return 1;
    }
    else if (n==2){
        return 2;
    }
    else{
        return ways(n-1)+ways(n-2)+ways(n-3);
    }
}

int main()
{
    int n;
    cout<<"Enter number of steps"<<endl;
    cin>>n;
    cout<<ways(n)<<" ways"<<endl;
    return 0;
}