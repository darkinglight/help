#include <stdio.h>
#include "intepret.h"
#include "util.h"

A_stm A_CompoundStm(A_stm stm1, A_stm stm2) {
    A_stm s = checked_malloc(sizeof(*s));
    s->kind = A_compoundStm;
    s->u.compound.stm1 = stm1;
    s->u.compound.stm2 = stm2;
    return s;
}

A_stm A_AssignStm(string id, A_exp exp) {
    A_stm s = checked_malloc(sizeof(*s));
    s->kind = A_assignStm;
    s->u.assign.id = id;
    s->u.assign.exp = exp;
    return s;
}

A_stm A_PrintStm(A_expList exps) {
    A_stm s = checked_malloc(sizeof(*s));
    s->kind = A_printStm;
    s->u.print.exps = exps;
    return s;
}

A_exp A_IdExp(string id) {
    A_exp e = checked_malloc(sizeof(*e));
    e->kind = A_idExp;
    e->u.id = id;
    return e;
}

A_exp A_NumExp(int num) {
    A_exp e = checked_malloc(sizeof(*e));
    e->kind = A_numExp;
    e->u.num = num;
    return e;
}

A_exp A_OpExp(A_exp left, A_binop oper, A_exp right) {
    A_exp e = checked_malloc(sizeof(*e));
    e->kind = A_opExp;
    e->u.op.left = left;
    e->u.op.oper = oper;
    e->u.op.right = right;
    return e;
}

A_exp A_EseqExp(A_stm stm, A_exp exp) {
    A_exp e = checked_malloc(sizeof(*e));
    e->kind = A_eseqExp;
    e->u.eseq.stm = stm;
    e->u.eseq.exp = exp;
    return e;
}

A_expList A_PairExpList(A_exp head, A_expList tail) {
    A_expList l = checked_malloc(sizeof(*l));
    l->kind = A_pairExpList;
    l->u.pair.head = head;
    l->u.pair.tail = tail;
    return l;
}

A_expList A_LastExpList(A_exp last) {
    A_expList l = checked_malloc(sizeof(*l));
    l->kind = A_lastExpList;
    l->u.last = last;
    return l;
}

int maxargsExp(A_exp e) {
    int num = 0;
    if (e->kind == A_opExp) {
        int left = maxargsExp(e->u.op.left);
        int right = maxargsExp(e->u.op.right);
        num += left + right;
    } else if (e->kind == A_eseqExp) {
        int left = maxargs(e->u.eseq.stm);
        int right = maxargsExp(e->u.eseq.exp);
        num += left + right;
    }
    return num;
}

int maxargsExpList(A_expList list) {
    int num = 0;
    if (list->kind == A_pairExpList) {
        int first = maxargsExp(list->u.pair.head);
        int second = maxargsExpList(list->u.pair.tail);
        num += first + second;
    } else {
        num = maxargsExp(list->u.last);
    }
    return num;
}

int maxargs(A_stm s) {
    int num = 0;
    if (s->kind == A_compoundStm) {
        int first = maxargs(s->u.compound.stm1);
        int second = maxargs(s->u.compound.stm2);
        num += first + second;
    } else if (s->kind == A_printStm) {
        A_expList list = s->u.print.exps;
        num = 1 + maxargsExpList(list);
    } else {
        A_exp exp = s->u.assign.exp;
        num = maxargsExp(exp);
    }
    return num;
}

int load(string key, table t) {
    while (t != NULL && t->key != key) {
        t = t->next;
    }
    if (t == NULL) {
        perror("符号表数据缺失");
        exit(-1);
    }
    return t->value;
}
void save(string key, int value, table t) {
    table n = checked_malloc(sizeof(*n));
    n->key = key;
    n->value = value;
    n->next = t;
    t = n;
}

int interpExp(A_exp e, table t) {
    int result, left, right;
    switch (e->kind) {
        case A_idExp:
            result = load(e->u.id, t);
            break;
        case A_numExp:
            result = e->u.num;
            break;
        case A_opExp:
            left = interpExp(e->u.op.left, t);
            right = interpExp(e->u.op.right, t);
            switch (e->u.op.oper) {
                case A_plus:
                    result = left + right;
                    break;
                case A_minus:
                    result = left - right;
                    break;
                case A_times:
                    result = left * right;
                    break;
                case A_div:
                    result = left / right;
                    break;
            }
            break;
        case A_eseqExp:
            interpStm(e->u.eseq.stm, t);
            result = interpExp(e->u.eseq.exp, t);
            break;
    }
    return result;
}

void interpStm(A_stm s, table t) {
    int value;
    A_expList exps;
    switch (s->kind) {
        case A_compoundStm:
            interpStm(s->u.compound.stm1, t);
            interpStm(s->u.compound.stm2, t);
            break;
        case A_assignStm:
            value = interpExp(s->u.assign.exp, t);
            save(s->u.assign.id, value, t);
            break;
        case A_printStm:
            exps = s->u.print.exps;
            while (exps->kind == A_pairExpList) {
                value = interpExp(exps->u.pair.head, t);
                printf("%d", value);
                exps = exps->u.pair.tail;
            }
            value = interpExp(exps->u.last, t);
            printf("%d", value);
            break;
    }
}

void interp(A_stm s) {
    interpStm(s, NULL);
}
