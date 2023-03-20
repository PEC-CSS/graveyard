#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    int row[T];
    int column[T];
    int min_energy;
    for(int i  = 0; i<T;i++)
    {
    cin>>row[i]>>column[i];
    }
    for(int i = 0;i<T;i++)
    {
    if (row[i]<column[i]){
        min_energy = (2*row[i])+column[i]-2;
    }
    else
    {
        min_energy = row[i]+(column[i]*2)-2;
    }
    cout<<min_energy<<endl;
    }
    return 0;
}