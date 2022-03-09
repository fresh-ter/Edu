#include <iostream>

using namespace std;

int a[10][10] = {
        {1,2,5,3,6,4,6,3,6,4},
        {5,5,3,6,3,6,4,3,8,6},
        {6,4,0,6,5,4,6,3,4,5},
        {6,4,7,8,3,1,3,3,1,3},
        {1,7,5,8,0,7,4,6,5,6},
        {7,9,4,7,0,3,2,5,3,2},
        {7,2,3,4,6,3,5,5,1,2},
        {0,5,0,4,5,6,4,4,5,2},
        {4,0,0,1,3,5,5,6,3,7},
        {0,4,0,5,6,3,5,2,4,1}
};

int getMin(int i, int j, int val) {
    if(a[i][j] < val)
        return a[i][j];
    else
        return val;
}

bool isLocMin(int i, int j) {
    int min_val = a[i][j];

    if(i==0 && j==0) {
        min_val = getMin(i, j+1, min_val);
        min_val = getMin(i+1, j+1, min_val);
        min_val = getMin(i+1, j, min_val);
    }
    else if(i==9 && j==9) {
        min_val = getMin(i, j-1, min_val);
        min_val = getMin(i-1, j-1, min_val);
        min_val = getMin(i-1, j, min_val);
    }
    else if(i==0 && j==9) {
        min_val = getMin(i+1, j, min_val);
        min_val = getMin(i+1, j-1, min_val);
        min_val = getMin(i, j-1, min_val);
    }
    else if(i==9 && j==0) {
        min_val = getMin(i-1, j, min_val);
        min_val = getMin(i-1, j+1, min_val);
        min_val = getMin(i, j+1, min_val);
    }
        // top
    else if(i==0) {
        min_val = getMin(i, j+1, min_val);
        min_val = getMin(i+1, j+1, min_val);
        min_val = getMin(i+1, j, min_val);
        min_val = getMin(i+1, j-1, min_val);
        min_val = getMin(i, j-1, min_val);
    }
        // down
    else if(i==9) {
        min_val = getMin(i, j-1, min_val);
        min_val = getMin(i-1, j-1, min_val);
        min_val = getMin(i-1, j, min_val);
        min_val = getMin(i-1, j+1, min_val);
        min_val = getMin(i, j+1, min_val);
    }
        //left
    else if(j==0) {
        min_val = getMin(i-1, j, min_val);
        min_val = getMin(i-1, j+1, min_val);
        min_val = getMin(i, j+1, min_val);
        min_val = getMin(i+1, j+1, min_val);
        min_val = getMin(i+1, j, min_val);
    }
        //right
    else if(j==9) {
        min_val = getMin(i+1, j, min_val);
        min_val = getMin(i+1, j-1, min_val);
        min_val = getMin(i, j-1, min_val);
        min_val = getMin(i-1, j-1, min_val);
        min_val = getMin(i-1, j, min_val);
    }
    else {
        min_val = getMin(i-1, j, min_val);
        min_val = getMin(i-1, j+1, min_val);
        min_val = getMin(i, j+1, min_val);
        min_val = getMin(i+1, j+1, min_val);
        min_val = getMin(i+1, j, min_val);

        min_val = getMin(i+1, j-1, min_val);
        min_val = getMin(i, j-1, min_val);
        min_val = getMin(i-1, j-1, min_val);
    }

    if(a[i][j] == min_val)
        return true;
    else
        return false;
}

int main()
{
    for(auto & i : a)
    {
        for(int j : i)
        {
            cout << j << ' ';
        }
        cout << endl;
    }
    cout << endl << endl;

    int locMinCounter = 0;
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            if(isLocMin(i,j))
                locMinCounter += 1;

        }
    }

    int i,j;

    cout << "Number of locMin: " << locMinCounter << endl;

    cout << "Enter i: ";
    cin >> i;
    cout << "Enter j: ";
    cin >> j;
    cout << "isLocMin: " << isLocMin(i,j) << endl << endl;

    //cout << "Hello world!" << endl;
    return 0;
}