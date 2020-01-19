#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <arpa/inet.h>

int main(int argc, char **argv)
{
    struct in_addr inaddr;
    if (argc != 2) {
        fprintf(stderr, "%s ip\n", argv[0]);
        exit(0);
    }

    inet_pton(AF_INET, argv[1], &inaddr);
    uint32_t addr = ntohl(inaddr.s_addr);
    printf("0x%x\n", addr);
    exit(0);
}
