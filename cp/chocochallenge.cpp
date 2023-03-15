#include <iostream>
#include <math.h>
#include <climits>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    int xor_sum= 0;
    int max_chocs = 0;
    int count_max_chocs = INT_MIN;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        xor_sum ^= a[i];

        if (a[i] > max_chocs)
        {
            max_chocs = a[i];
            count_max_chocs = max(count_max_chocs,a[i]);
        }
    }
    if (xor_sum == 0)
    {
        cout << "0" << endl;
    }
    else
    {
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            int temp = xor_sum ^ a[i];
            if (temp <= a[i])
            {
                count++;
            }
        }
        cout << count << endl;
    }
    return 0;
}
