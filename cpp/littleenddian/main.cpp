#include <iostream>

using namespace std;

int main() {
    unsigned long long data = 0x11223344;
    char text[8];
    sprintf(text, "0x%.8x", data);
    cout << "data = " << text << endl;
    char tmp[8];
    char *p = (char *)&data;
    for (int i = 0; i < 4; i++) {
        sprintf(tmp, "0x%.2x", *(p + i));
        cout << "data[" << i << "] = " << tmp << endl;
    }
    return 0;
}
