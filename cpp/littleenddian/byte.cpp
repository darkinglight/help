#include <iostream>
using namespace std;

int main() {
    int v = 1;
    int *p = &v;
    cout << p << endl;
    cout << p + 1 << endl;
    cout << sizeof(char *) << endl;
    return 0;
}
