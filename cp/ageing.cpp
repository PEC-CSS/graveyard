#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    int x[T];
    for(int i = 0;i<T;i++)
    {
            {
                cin>>x[i];
            }
    }
    for(int j = 0; j<T;j++)
        {
            cout<<x[j]-10<<endl;
        }
    return 0;
}