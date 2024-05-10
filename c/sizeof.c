#include <stdio.h>
#include <stdint.h>

struct redisObject {
    unsigned type:4;
    unsigned encoding:4;
    unsigned lru:24;
    int refcount;
    void *ptr;
};

struct __attribute__ ((__packed__)) sdshdr8 {
    uint8_t len; /* used */
    uint8_t alloc; /* excluding the header and null terminator */
    unsigned char flags; /* 3 lsb of type, 5 unused bits */
    char buf[];
};

void main(int argc, char **args) {
    int a = 10;
    int *p = &a;
    printf("size of int = %lu bytes", sizeof(a));
    struct redisObject *o;
    printf("\nsize of redisObject point = %lu bytes", sizeof(o));
    printf("\nsize of sdshdr8 = %lu bytes", sizeof(struct sdshdr8));
}
