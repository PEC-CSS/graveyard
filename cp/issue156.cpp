#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;
    
    int x;
    x = floor(n/2); 
    if(n%2 == 1){
        if(x%2==1){
            cout << '0' << endl;
        }
        else{
            cout<<'1'<<endl;
        }
        
    }
    else{
        if(x%2==0){
            cout << '0' << endl;
        }
        else{
            cout<<'1'<<endl;
        }
    }

}