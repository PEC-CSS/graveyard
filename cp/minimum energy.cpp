#include<iostream>
using namespace std;
int main()
{
    int rows,columns,min_energy;
    cin>>rows>>columns;
    if (rows<columns){
        min_energy = (2*rows)+columns-2;
    }
    else
    {
        min_energy = rows+(columns*2)-2;
    }
    cout<<min_energy;

    return 0;
}