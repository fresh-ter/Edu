#include <iostream>

using namespace std;

struct MARSH {
    string start;
    string stop;
    int num{};
};

void update(MARSH *e) {
    cout << "Enter <start name> :";
    cin >> e->start;
    cout << "Enter <stop name> :";
    cin >> e->stop;
    cout << "Enter <num> :";
    cin >> e->num;
}

void show(MARSH *e) {
    cout << "<start name> :" << e->start << endl;
    cout << "<stop name> :" << e->stop << endl;
    cout << "<num> :" << e->num << endl;
}

int main()
{
    MARSH arr[8];

    for(int x=0; x<8; x++) {
        cout << "-----------------------------------------------" << endl;
        cout << "Edit " << x+1 <<" MARSH" << endl << endl;

        update(&arr[x]);
    }

    cout << "=============================================" << endl << endl;
    cout << "Enter <num> for search:";
    int s;
    cin >> s;

    bool stat = false;

    for(auto & x : arr) {
        if(x.num == s){
            show(&x);
            stat = true;
        }
    }
    if(!stat) {
        cout << "404 - Not Found!";
    }

    return 0;
}
