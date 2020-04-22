typedef char *String;
typedef enum {INIT, ID, IF, SPACE} Type;

struct table {
    Type type;
    String value;
    struct table *next;
};
struct table *header, *tail;

struct state {
    char *input;
    struct state **next;
    Type type;
};

void scan(String);
