#include <iostream>
using namespace std;
int main(){
    int t,n,val;
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>n;
        int Odd[n];
        int Even[n];
        int cod=0,ceve=0;
        for (int i=0; i<n; i++){
            cin>>val;
            if(val%2==0){
                Even[ceve]=i+1;
                ceve++;
            }
            else{
                Odd[cod]=i+1;
                cod++;
            }
        }
        if(n<3)
            cout<<"NO";
        else{
            if((cod>=3)){
                cout<<"YES"<<endl;
                for(int i=0; i<3; i++){
                    cout<<Odd[i]<<" ";
                }
                cout<<endl;
            }
            else if(cod>=1 && ceve>=2){
                cout<<"YES"<<endl;
                for(int i=0; i<2; i++){
                    cout<<Even[i]<<" ";
                }
                cout<<Odd[0]<<endl;
            }
            else
                cout<<"NO"<<endl;
        }
    }
}