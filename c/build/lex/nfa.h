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
    struct state *next[27];
    Type type;
};

void scan(String);
