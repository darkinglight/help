#include "paddr.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Usage: %s hostname\n", argv[1]);
        exit(1);
    }
    print_addr(argv[1]);
    exit(0);
}
