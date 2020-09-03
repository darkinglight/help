#include <stdio.h>

int main(int argc, char **argv) {
    int v = 1;
    int *p = &v;
    printf("p's address is %p\n", p);
    p++;
    printf("p++'s address is %p\n", p);
    printf("p's size is %ld\n", sizeof(p));
    char *pchar = (char *)p;
    size_t i;
    size_t len = sizeof(p);
    for (i = 0; i < len; i++) {
        printf(" %.2x", pchar[i]);
    }
    return 0;
}
