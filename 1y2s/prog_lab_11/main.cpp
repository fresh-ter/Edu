#include <iostream>

using namespace std;

int main()
{
    int L[10] = {1,56,3,7,3,76,4,7,3,3};

    int max_number=0;
    int max_count=0;
    int counter;

    for(int c : L) {
        cout << c << ' ';
    }
    cout << endl << endl;

    for(int c : L) {
        counter = 0;

        for(int i : L) {
            if(c == i) {
                counter++;
            }
        }

        if(counter > max_count) {
            max_count = counter;
            max_number = c;
        }
    }

    cout << "max_number: " << max_number << endl;
    cout << "max_count: " << max_count << endl;

    int L2[10-max_count];
    int index=0;

    for(int c : L) {
        if(c != max_number) {
            L2[index] = c;
            index++;
        }
    }
    cout << endl;

    for(int c = 0; c<10-max_count; c++) {
        cout << L2[c] << ' ';
    }
    cout << endl << endl;

    return 0;
}
