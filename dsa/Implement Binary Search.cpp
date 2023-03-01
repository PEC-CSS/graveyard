#include <iostream>
using namespace std;

int binarySearch(int nums[], int size, int target)
{
    int start = 0;
    int end = size - 1;
    int mid = (start + end) / 2;

    while (start <= end)
    {
        if (nums[mid] == target)
        {
            return mid;
        }

        else if (nums[mid] > target)
        {
            end = mid -1;
            mid = (start + end) / 2;
        }

        else
        {
            start = mid + 1;
            mid = (start + end) / 2;
        }
    }

    return -1;
}

int main()
{
    int nums1[6] = {1, 2, 3, 5, 9, 12};
    int target1 = 3;

    int nums2[4] = {6, 18 ,30 ,45};
    int target2 = 9;

    cout << binarySearch(nums1, 6, target1) << endl;
    cout << binarySearch(nums2, 4, target2) << endl;

    return 0;
}