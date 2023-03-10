#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1, s2;
    cout << "Enter first string: ";
    cin >> s1;
    cout << "Enter second string: ";
    cin >> s2;
    if (s1.length() != s2.length()) {
        cout << "No" << endl;
        return 0;
    }
    string s3 = s1 + s1;
    if (s3.find(s2) != string::npos) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
