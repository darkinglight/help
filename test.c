#include <sys/socket.h>
#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
int main(int argc, char **argv)
{
    int n;
    if (inet_pton(AF_INET, "192.168.0.1", &n) <= 0) {
        fprintf(stderr, "my error");
    }
    fprintf(stdout, "%d\n\a", n);
    exit(0);
}
