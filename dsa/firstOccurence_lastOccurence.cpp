//Finding the first occurence and last occurence of a number
# include <iostream>
using namespace std;
void binarySearch(int n,long search[], long x,long *ArrayList){
    int F=0;
    int ind;
    int L;
    L=n;
    int middle;
    int pos=-1;
    while(F<=L){
        middle=(F+L)/2;
        if (search[middle]==x){
            pos=middle;
            ind=pos-1;
            while(search[ind]==x && ind>=0){
                ind = ind-1;
            }
            ArrayList[0]=ind+1;
            ind=pos+1;
            while(search[ind]==x && ind<n){
                ind = ind+1;
            }
            ArrayList[1]=ind-1;
            return;
        }
        else if (search[middle]<x){
            F=middle+1;
        }
        else{
            L=middle-1;
        }
    }
    ArrayList[0]=pos;
    ArrayList[1]=pos;
}
int main(){
    int n;
    long x;
    cout<<"Enter no. of elements ";
    cin>>n;
    long search[n];
    for (int i=0; i<n; i++){
        cout<<"Enter element "<<i+1;
        cin>>search[i];
    }
    cout<<"Enter item to be searched ";
    cin>>x;
    long ArrayList[2];
    binarySearch(n,search,x,ArrayList);
    for (int i=0; i<2; i++){
        cout<<ArrayList[i]<<" ";
    }
}