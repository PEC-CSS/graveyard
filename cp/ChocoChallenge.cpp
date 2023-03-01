#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    // Read the chocolate counts for each box
    vector<int> boxes(n);
    for (int i = 0; i < n; i++) {
        cin >> boxes[i];
    }

    // Calculate the sum of all box counts
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += boxes[i];
    }

    // Check if the first player can always win
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (boxes[i] >= sum - boxes[i]) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
