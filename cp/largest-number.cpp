#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  vector<int> list;
  int size;
  cout << "Enter size of list : ";
  cin >> size;
  for (int i=0; i<size; i++) {
    int x;
    cout << "Enter element to add : ";
    cin >> x;
    list.push_back(x);
  }
  sort(list.begin(), list.end(), greater<int>());
  for (int y : list) {
    cout << y;
  }
}
