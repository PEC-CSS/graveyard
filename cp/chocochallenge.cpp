#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    int xor_sum= 0;
    int max_chocs = 0;
    int count_max_chocs = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        xor_sum ^= a[i];

        if (a[i] > max_chocs)
        {
            max_chocs = a[i];
            count_max_chocs = 1;
        }
        else if (a[i] == max_chocs)
        {
            count_max_chocs++;
        }
    }
    if (xor_sum != 0 || count_max_chocs > 1)
    {
        cout << "0" << endl;
    }
    else
    {
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] == max_chocs)
            {
                count++;
            }
        }
        cout << count << endl;
    }
    return 0;
}
