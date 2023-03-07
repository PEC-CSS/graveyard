#include <iostream>
using namespace std;
void Divide(long *a,int n){
    int check = 0;
    for(int i=0; i<n; i++){
        a[i]++;
        long x = a[i];
        if((x%(a[i-1])==0 || (a[i-1])%x==0) && i>0){
            a[i]++;
        }
        check++;
        if(check==2*n)
            break;
    }
}
int main(){
    int n;
    cin>>n;
    long a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    Divide(a,n);
    for(int i=0; i<n; i++){
        cout<<a[i]<<" ";
    }
}
