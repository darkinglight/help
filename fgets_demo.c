#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int size = 1024;
    char* buffer = (char*)malloc(size);

    while (NULL != fgets(buffer, size, stdin)) {
        printf("Read line with len: %d\n", strlen(buffer));
        printf("%s", buffer);
    }

    free(buffer);
}
