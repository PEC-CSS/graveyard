#include <iostream>
using namespace std;
void Divide(int *a,int n){
    int check = 0;
    for(int i=0; i<n; i++){
        int x = a[i];
        a[i]++;
        if((a[i]+1)%x==0){
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
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    Divide(a,n);
    for(int i=0; i<n; i++){
        cout<<a[i]<<" ";
    }
}