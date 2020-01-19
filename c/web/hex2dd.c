#include "unixerr.h"
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <arpa/inet.h>

#define MAXBUF 128

int main(int argc, char **argv)
{
    struct in_addr inaddr;
    uint32_t addr;
    char buf[MAXBUF];

    if (argc != 2) {
        fprintf(stderr, "usage:%s <hex number>\n", argv[0]);
    }

    sscanf(argv[1], "%x", &addr);
    inaddr.s_addr = htonl(addr);
    if (!inet_ntop(AF_INET, &inaddr, buf, MAXBUF))
        unix_error("inet_ntop");
    printf("%s\n", buf);

    exit(0);
}
