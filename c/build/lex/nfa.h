typedef char *String;
typedef enum {INIT, ID, IF, SPACE} Type;

struct table {
    Type type;
    String value;
    struct table *next;
};
struct table *header, *tail;

struct state {
    char input[27];
    Type type;
    struct state *next[27];
};

void scan(String);
