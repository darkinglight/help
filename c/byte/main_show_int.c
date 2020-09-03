void show_int(int);
void show_float(float);
void show_pointer(void *);

void test_show_bytes(int val) {
    int ival = val;
    float fval = (float) ival;
    int *pval = &ival;
    show_int(ival);
    show_float(fval);
    show_pointer(pval);
}

int main() {
    test_show_bytes(1);
    test_show_bytes(1024);
}
