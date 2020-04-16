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
        num = maxargsExpList(list);
    } else {
        A_exp exp = s->u.assign.exp;
        num = maxargsExp(exp);
    }
    return num;
}
