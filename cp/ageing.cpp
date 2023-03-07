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
    for(int i = 0; i<T;i++)
        {
            cout<<x[i]-10<<endl;
        }
    return 0;
}