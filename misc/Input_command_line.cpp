#include <iostream>
using namespace std;
int main(int argc, char **argv){
    int max = 0;
    for(int i=1; i<argc; i++){
        if(atoi(argv[i])>max){
            max = atoi(argv[i]);
        }
    }
    cout<<max;
    return 0;
}
