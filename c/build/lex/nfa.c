#include <stdlib.h>
#include <stdio.h>
#include "nfa.h"

//             --       i       if     [^if]     [ \t\n]
struct state state0, state1, state2, state3, state4;
void init() {
    state0.type = INIT;
//    state1->type = ID;
//    state2->type = IF;
//    state3->type = ID;
//    state4->type = SPACE;

//    state0->input = (char*)malloc(27*sizeof(char));
//    state1->input = (char*)malloc(27*sizeof(char));
//    state2->input = (char*)malloc(27*sizeof(char));
//    state3->input = (char*)malloc(27*sizeof(char));
//    state4->input = (char*)malloc(27*sizeof(char));
//
//    state0->next = (struct state**)malloc(27*sizeof(struct state*));
//    state1->next = (struct state**)malloc(27*sizeof(struct state*));
//    state2->next = (struct state**)malloc(27*sizeof(struct state*));
//    state3->next = (struct state**)malloc(27*sizeof(struct state*));
//    state4->next = (struct state**)malloc(27*sizeof(struct state*));

    for (int i = 0; i < 26; i++) {
        state0.input[i] = 'a' + i;
//        state0->next[i] = state3;
//
//        state1->input[i] = 'a' + i;
//        state1->next[i] = state3;
//
//        state2->input[i] = 'a' + i;
//        state2->next[i] = state3;
//        
//        state3->input[i] = 'a' + i;
//        state3->next[i] = state3;
//
//        state4->input[i] = 'a' + i;
//        state4->next[i] = state0;
    }
    
//    state0->input[26] = ' ';
//    state0->next[26] = state0;
//    state0->next[8] = state1;
//
//    state1->input[26] = ' ';
//    state1->next[26] = state0;
//    state1->next[5] = state2;
//
//    state2->input[26] = ' ';
//    state2->next[26] = state0;
//
//    state3->input[26] = ' ';
//    state3->next[26] = state0;
//
//    state4->input[26] = ' ';
//    state4->next[26] = state4;
}

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
    init();
    scan(args[1]);
    return 0;
}
