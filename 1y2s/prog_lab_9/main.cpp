#include <iostream>

using namespace std;

struct MARSH {
    string start;
    string stop;
    int num{};
};

int main()
{
    MARSH arr[8];

    for(int x=0; x<8; x++) {
        cout << "-----------------------------------------------" << endl;
        cout << "Edit " << x+1 <<" MARSH" << endl << endl;

        cout << "Enter <start name> :";
        cin >> arr[x].start;
        cout << "Enter <stop name> :";
        cin >> arr[x].stop;
        cout << "Enter <num> :";
        cin >> arr[x].num;
    }

    cout << "=============================================" << endl << endl;
    cout << "Enter <num> for search:";
    int s;
    cin >> s;

    bool stat = false;

    for(auto & x : arr) {
        if(x.num == s){
            cout << "<start name> :" << x.start << endl;
            cout << "<stop name> :" << x.stop << endl;
            cout << "<num> :" << x.num << endl;

            stat = true;
        }
    }

    if(!stat) {
        cout << "404 - Not Found!";
    }

    return 0;
}
