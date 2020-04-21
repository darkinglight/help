typedef char *String;
typedef enum {ID, IF} Type;

struct table {
    Type type;
    String value;
    struct table *next;
};
struct table *header, *tail;

void scan(String);
