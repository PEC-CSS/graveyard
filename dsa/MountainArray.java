package dsa;

public class MountainArray {
    public static int findInMountainArray(int target, int mountainArr[]) {
        int i = -1;
        int peak = binSrchPk(mountainArr);
        i = binSrch(mountainArr, 0, peak, target, true);
        if(i != -1) {
            return i;
        }
        return binSrch(mountainArr, peak, mountainArr.length - 1, target, false);
    }

    public static int binSrch(int mountainArr[], int l, int r, int target, boolean asc) {
        while(l <= r) {
            int mid = (l + r)/2;
            int midval = mountainArr[mid];
            if(midval == target) {
                return mid;
            }
            if(midval <= target) {
                if(asc) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
                continue;
            }
            if(asc) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }

    public static int binSrchPk(int mountainArr[]) {
        int l = 0, r = mountainArr.length - 1;
        while(l <= r) {
            int mid = (l + r)/2;
            int midval = mountainArr[mid];
            int midvall = mountainArr[mid - 1];
            int midvalr = mountainArr[mid + 1];
            if(midvall <= midval && midval >= midvalr) {
                return mid;
            }
            if(midvall <= midval && midval <= midvalr) {
                l = mid;
                continue;
            }
            r = mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findInMountainArray(7, new int[]{1,2,3,4,5,3,1}));
    }
}