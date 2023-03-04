#include <iostream>
using namespace std;
int main(int argc, char **argv){
    if (argc<2){
        cout<<0;
    }
    else{
        int max = 0;
        for(int i=1; i<argc; i++){
            if(atoi(argv[i])>max){
                max = atoi(argv[i]);
            }
        }
        cout<<max;
    } 
    return 0;
}