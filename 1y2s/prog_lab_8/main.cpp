#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    string s = "Hello world!";
    string s1;

    for(int x=0; x<strlen(&s[0]); x+=2)
        s1 += s[x];

    cout << s << endl;
    cout << s1 << endl;

    return 0;
}
