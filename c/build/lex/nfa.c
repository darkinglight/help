#include <stdlib.h>
#include <stdio.h>
#include "nfa.h"

void scan(String filename) {
    int c;
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("fail open file");
        exit(1);
    }

    while(1) {
        c = fgetc(fp);
        if ( feof(fp) ) {
            break;
        }
        printf("%c", c);
    }

    fclose(fp);
}

int main(int argc, char **args) {
    scan(args[1]);
    return 0;
}
