#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>

int main (int argc, char **argv) 
{
    int opt;
    int digit_optind = 0;
    int option_index = 0;
    char *optstring = "a:b:c:d";
    static struct option long_options[] = {
        {"reqarg", required_argument, NULL, 'r'},
        {"noarg", no_argument, NULL, 'n'},
        {"optarg", optional_argument, NULL, 'o'},
    }
}
