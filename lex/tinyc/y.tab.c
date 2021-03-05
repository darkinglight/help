/* A Bison parser, made by GNU Bison 3.3.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2019 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.3.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 1 "parser.y" /* yacc.c:337  */

#include <stdio.h>
#include <stdlib.h>
void yyerror(const char*);
#define YYSTYPE char *

int ii = 0, itop = -1, istack[100];
int ww = 0, wtop = -1, wstack[100];

#define _BEG_IF     {istack[++itop] = ++ii;}
#define _END_IF     {itop--;}
#define _i          (istack[itop])

#define _BEG_WHILE  {wstack[++wtop] = ++ww;}
#define _END_WHILE  {wtop--;}
#define _w          (wstack[wtop])


#line 89 "y.tab.c" /* yacc.c:337  */
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "y.tab.h".  */
#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    T_Int = 258,
    T_Void = 259,
    T_Return = 260,
    T_Print = 261,
    T_ReadInt = 262,
    T_While = 263,
    T_If = 264,
    T_Else = 265,
    T_Break = 266,
    T_Continue = 267,
    T_Le = 268,
    T_Ge = 269,
    T_Eq = 270,
    T_Ne = 271,
    T_And = 272,
    T_Or = 273,
    T_IntConstant = 274,
    T_Identifier = 275,
    T_StringConstant = 276
  };
#endif
/* Tokens.  */
#define T_Int 258
#define T_Void 259
#define T_Return 260
#define T_Print 261
#define T_ReadInt 262
#define T_While 263
#define T_If 264
#define T_Else 265
#define T_Break 266
#define T_Continue 267
#define T_Le 268
#define T_Ge 269
#define T_Eq 270
#define T_Ne 271
#define T_And 272
#define T_Or 273
#define T_IntConstant 274
#define T_Identifier 275
#define T_StringConstant 276

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */



#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && ! defined __ICC && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  2
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   217

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  37
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  34
/* YYNRULES -- Number of rules.  */
#define YYNRULES  71
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  128

#define YYUNDEFTOK  2
#define YYMAXUTOK   276

/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                                \
  ((unsigned) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    30,     2,     2,     2,    29,     2,     2,
      31,    32,    27,    25,    35,    26,     2,    28,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,    36,
      23,    22,    24,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    33,     2,    34,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint8 yyrline[] =
{
       0,    35,    35,    36,    39,    42,    43,    47,    51,    52,
      56,    57,    61,    62,    66,    67,    71,    72,    76,    77,
      78,    79,    80,    81,    82,    83,    86,    90,    94,    95,
      99,   103,   107,   108,   112,   113,   117,   118,   122,   126,
     130,   134,   138,   142,   146,   150,   154,   158,   162,   166,
     170,   175,   176,   177,   178,   179,   180,   181,   182,   183,
     184,   185,   186,   187,   188,   189,   190,   191,   192,   193,
     194,   198
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "T_Int", "T_Void", "T_Return", "T_Print",
  "T_ReadInt", "T_While", "T_If", "T_Else", "T_Break", "T_Continue",
  "T_Le", "T_Ge", "T_Eq", "T_Ne", "T_And", "T_Or", "T_IntConstant",
  "T_Identifier", "T_StringConstant", "'='", "'<'", "'>'", "'+'", "'-'",
  "'*'", "'/'", "'%'", "'!'", "'('", "')'", "'{'", "'}'", "','", "';'",
  "$accept", "Program", "FuncDecl", "RetType", "FuncName", "Args", "_Args",
  "VarDecls", "VarDecl", "Stmts", "Stmt", "AssignStmt", "PrintStmt",
  "PActuals", "CallStmt", "CallExpr", "Actuals", "ReturnStmt", "IfStmt",
  "TestExpr", "StmtsBlock", "If", "Then", "EndThen", "Else", "EndIf",
  "WhileStmt", "While", "Do", "EndWhile", "BreakStmt", "ContinueStmt",
  "Expr", "ReadInt", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,    61,    60,    62,    43,    45,    42,    47,    37,
      33,    40,    41,   123,   125,    44,    59
};
# endif

#define YYPACT_NINF -87

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-87)))

#define YYTABLE_NINF -1

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     -87,     5,   -87,   -87,   -87,   -87,    -7,   -87,    10,    45,
      24,    28,    35,   -87,    29,    60,   -87,    46,    70,   -87,
      56,    -1,    31,   -87,    57,   -87,    38,    48,   -87,   -87,
      44,    49,   -16,   -87,   -87,   -87,   -87,   -87,    58,   -87,
     -87,    50,   -87,    50,   -87,   -87,   -87,    53,   -87,    61,
      52,    52,    52,   -87,   -87,    73,   -87,    72,   -87,   -87,
      52,    52,   -87,    52,   -87,   -87,    89,   -87,   -87,   107,
      52,    52,    52,    52,    52,    52,    52,    52,    52,    52,
      52,    52,    52,   -87,   -87,    90,    79,   147,   127,    94,
      94,    80,   -87,    -9,    -9,   188,   188,   181,   164,    -9,
      -9,    27,    27,   -87,   -87,   -87,   -25,   -87,   -87,    93,
     -87,   -87,   -87,   -87,   -87,   101,    52,    41,   119,   -87,
     -87,   147,   -87,   -87,    94,   -87,   -87,   -87
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       2,     0,     1,     5,     6,     3,     0,     7,     0,     8,
       0,     0,     9,    10,     0,     0,    12,     0,    16,    11,
       0,     0,     0,    14,     0,    13,     0,     0,    46,    40,
       0,     0,     0,     4,    17,    18,    19,    20,     0,    21,
      22,     0,    23,     0,    24,    25,    15,     0,    66,    67,
       0,     0,     0,    35,    69,     0,    68,     0,    49,    50,
       0,    32,    30,     0,    41,    47,     0,    64,    65,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    34,    28,     0,     0,    28,     0,     0,
       0,     0,    70,    59,    58,    60,    61,    63,    62,    57,
      56,    51,    52,    53,    54,    55,     0,    26,    31,    33,
      38,    16,    42,    48,    71,     0,     0,     0,    44,    45,
      27,    29,    39,    43,     0,    36,    44,    37
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -87,   -87,   -87,   -87,   -87,   -87,   -87,   -87,   -87,    36,
     -87,   -87,   -87,    51,   -87,   -22,   -87,   -87,   -87,   103,
     -86,   -87,   -87,   -87,   -87,    22,   -87,   -87,   -87,   -87,
     -87,   -87,   -49,   -87
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
      -1,     1,     5,     6,     8,    11,    12,    18,    21,    22,
      34,    35,    36,   106,    37,    54,    86,    39,    40,    64,
     112,    41,    89,   118,   124,   125,    42,    43,    90,   119,
      44,    45,    55,    56
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_uint8 yytable[] =
{
      38,    67,    68,    69,   113,     2,    60,   115,     3,     4,
     116,    85,    87,     7,    88,    61,    78,    79,    80,    81,
      82,    93,    94,    95,    96,    97,    98,    99,   100,   101,
     102,   103,   104,   105,    24,    25,    26,    27,   126,    28,
      29,     9,    30,    31,    13,    47,    26,    27,    10,    28,
      29,    32,    30,    31,    80,    81,    82,    48,    49,    47,
      14,    32,    16,    17,    50,    33,    19,   121,    51,    52,
      15,    48,    49,    20,    53,   122,    23,    46,    50,    57,
      58,    63,    51,    52,    66,    59,    70,    71,    72,    73,
      74,    75,    61,    84,    62,    38,    76,    77,    78,    79,
      80,    81,    82,    70,    71,    72,    73,    74,    75,    83,
      91,   108,   114,    76,    77,    78,    79,    80,    81,    82,
      70,    71,    72,    73,    74,    75,   107,   111,   116,   123,
      76,    77,    78,    79,    80,    81,    82,   120,   109,    92,
      70,    71,    72,    73,    74,    75,    65,   117,   127,     0,
      76,    77,    78,    79,    80,    81,    82,     0,     0,   110,
      70,    71,    72,    73,    74,    75,     0,     0,     0,     0,
      76,    77,    78,    79,    80,    81,    82,    70,    71,    72,
      73,    74,     0,     0,     0,     0,     0,    76,    77,    78,
      79,    80,    81,    82,    70,    71,    72,    73,     0,     0,
       0,    70,    71,     0,    76,    77,    78,    79,    80,    81,
      82,    76,    77,    78,    79,    80,    81,    82
};

static const yytype_int8 yycheck[] =
{
      22,    50,    51,    52,    90,     0,    22,    32,     3,     4,
      35,    60,    61,    20,    63,    31,    25,    26,    27,    28,
      29,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    35,    36,     5,     6,   124,     8,
       9,    31,    11,    12,    20,     7,     5,     6,     3,     8,
       9,    20,    11,    12,    27,    28,    29,    19,    20,     7,
      32,    20,    33,     3,    26,    34,    20,   116,    30,    31,
      35,    19,    20,     3,    36,    34,    20,    20,    26,    31,
      36,    31,    30,    31,    31,    36,    13,    14,    15,    16,
      17,    18,    31,    21,    36,   117,    23,    24,    25,    26,
      27,    28,    29,    13,    14,    15,    16,    17,    18,    36,
      21,    32,    32,    23,    24,    25,    26,    27,    28,    29,
      13,    14,    15,    16,    17,    18,    36,    33,    35,    10,
      23,    24,    25,    26,    27,    28,    29,    36,    87,    32,
      13,    14,    15,    16,    17,    18,    43,   111,   126,    -1,
      23,    24,    25,    26,    27,    28,    29,    -1,    -1,    32,
      13,    14,    15,    16,    17,    18,    -1,    -1,    -1,    -1,
      23,    24,    25,    26,    27,    28,    29,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    -1,    -1,    23,    24,    25,
      26,    27,    28,    29,    13,    14,    15,    16,    -1,    -1,
      -1,    13,    14,    -1,    23,    24,    25,    26,    27,    28,
      29,    23,    24,    25,    26,    27,    28,    29
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    38,     0,     3,     4,    39,    40,    20,    41,    31,
       3,    42,    43,    20,    32,    35,    33,     3,    44,    20,
       3,    45,    46,    20,    35,    36,     5,     6,     8,     9,
      11,    12,    20,    34,    47,    48,    49,    51,    52,    54,
      55,    58,    63,    64,    67,    68,    20,     7,    19,    20,
      26,    30,    31,    36,    52,    69,    70,    31,    36,    36,
      22,    31,    36,    31,    56,    56,    31,    69,    69,    69,
      13,    14,    15,    16,    17,    18,    23,    24,    25,    26,
      27,    28,    29,    36,    21,    69,    53,    69,    69,    59,
      65,    21,    32,    69,    69,    69,    69,    69,    69,    69,
      69,    69,    69,    69,    69,    69,    50,    36,    32,    50,
      32,    33,    57,    57,    32,    32,    35,    46,    60,    66,
      36,    69,    34,    10,    61,    62,    57,    62
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    37,    38,    38,    39,    40,    40,    41,    42,    42,
      43,    43,    44,    44,    45,    45,    46,    46,    47,    47,
      47,    47,    47,    47,    47,    47,    48,    49,    50,    50,
      51,    52,    53,    53,    54,    54,    55,    55,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    69,    69,    69,    69,    69,    69,    69,    69,
      69,    69,    69,    69,    69,    69,    69,    69,    69,    69,
      69,    70
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     2,     9,     1,     1,     1,     0,     1,
       2,     4,     0,     3,     2,     3,     0,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     4,     6,     0,     3,
       2,     4,     0,     2,     3,     2,     6,     8,     3,     3,
       1,     0,     0,     1,     0,     5,     1,     0,     0,     2,
       2,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     2,     2,     1,     1,     1,     1,
       3,     4
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YYUSE (yyoutput);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyo, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyo, yytype, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &yyvsp[(yyi + 1) - (yynrhs)]
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            else
              goto append;

          append:
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return (YYSIZE_T) (yystpcpy (yyres, yystr) - yyres);
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
                    yysize = yysize1;
                  else
                    return 2;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
    default: /* Avoid compiler warnings. */
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
      yysize = yysize1;
    else
      return 2;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yynewstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  *yyssp = (yytype_int16) yystate;

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    goto yyexhaustedlab;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = (YYSIZE_T) (yyssp - yyss + 1);

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
# undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 35 "parser.y" /* yacc.c:1652  */
    { /*empty*/ }
#line 1367 "y.tab.c" /* yacc.c:1652  */
    break;

  case 3:
#line 36 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1373 "y.tab.c" /* yacc.c:1652  */
    break;

  case 4:
#line 39 "parser.y" /* yacc.c:1652  */
    { printf("ENDFUNC\n\n"); }
#line 1379 "y.tab.c" /* yacc.c:1652  */
    break;

  case 5:
#line 42 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1385 "y.tab.c" /* yacc.c:1652  */
    break;

  case 6:
#line 43 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1391 "y.tab.c" /* yacc.c:1652  */
    break;

  case 7:
#line 47 "parser.y" /* yacc.c:1652  */
    { printf("FUNC @%s:\n", yyvsp[0]); }
#line 1397 "y.tab.c" /* yacc.c:1652  */
    break;

  case 8:
#line 51 "parser.y" /* yacc.c:1652  */
    { /*empty*/ }
#line 1403 "y.tab.c" /* yacc.c:1652  */
    break;

  case 9:
#line 52 "parser.y" /* yacc.c:1652  */
    { printf("\n\n"); }
#line 1409 "y.tab.c" /* yacc.c:1652  */
    break;

  case 10:
#line 56 "parser.y" /* yacc.c:1652  */
    { printf("arg %s", yyvsp[0]); }
#line 1415 "y.tab.c" /* yacc.c:1652  */
    break;

  case 11:
#line 57 "parser.y" /* yacc.c:1652  */
    { printf(", %s", yyvsp[0]); }
#line 1421 "y.tab.c" /* yacc.c:1652  */
    break;

  case 12:
#line 61 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1427 "y.tab.c" /* yacc.c:1652  */
    break;

  case 13:
#line 62 "parser.y" /* yacc.c:1652  */
    { printf("\n\n"); }
#line 1433 "y.tab.c" /* yacc.c:1652  */
    break;

  case 14:
#line 66 "parser.y" /* yacc.c:1652  */
    { printf("var %s", yyvsp[0]); }
#line 1439 "y.tab.c" /* yacc.c:1652  */
    break;

  case 15:
#line 67 "parser.y" /* yacc.c:1652  */
    { printf(", %s", yyvsp[0]); }
#line 1445 "y.tab.c" /* yacc.c:1652  */
    break;

  case 16:
#line 71 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1451 "y.tab.c" /* yacc.c:1652  */
    break;

  case 17:
#line 72 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1457 "y.tab.c" /* yacc.c:1652  */
    break;

  case 18:
#line 76 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1463 "y.tab.c" /* yacc.c:1652  */
    break;

  case 19:
#line 77 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1469 "y.tab.c" /* yacc.c:1652  */
    break;

  case 20:
#line 78 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1475 "y.tab.c" /* yacc.c:1652  */
    break;

  case 21:
#line 79 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1481 "y.tab.c" /* yacc.c:1652  */
    break;

  case 22:
#line 80 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1487 "y.tab.c" /* yacc.c:1652  */
    break;

  case 23:
#line 81 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1493 "y.tab.c" /* yacc.c:1652  */
    break;

  case 24:
#line 82 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1499 "y.tab.c" /* yacc.c:1652  */
    break;

  case 25:
#line 83 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1505 "y.tab.c" /* yacc.c:1652  */
    break;

  case 26:
#line 86 "parser.y" /* yacc.c:1652  */
    { printf("pop %s\n\n", yyvsp[-3]); }
#line 1511 "y.tab.c" /* yacc.c:1652  */
    break;

  case 27:
#line 90 "parser.y" /* yacc.c:1652  */
    { printf("print %s\n\n", yyvsp[-3]); }
#line 1517 "y.tab.c" /* yacc.c:1652  */
    break;

  case 28:
#line 94 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1523 "y.tab.c" /* yacc.c:1652  */
    break;

  case 29:
#line 95 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1529 "y.tab.c" /* yacc.c:1652  */
    break;

  case 30:
#line 99 "parser.y" /* yacc.c:1652  */
    { printf("pop\n\n"); }
#line 1535 "y.tab.c" /* yacc.c:1652  */
    break;

  case 31:
#line 103 "parser.y" /* yacc.c:1652  */
    { printf("$%s\n", yyvsp[-3]); }
#line 1541 "y.tab.c" /* yacc.c:1652  */
    break;

  case 32:
#line 107 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1547 "y.tab.c" /* yacc.c:1652  */
    break;

  case 33:
#line 108 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1553 "y.tab.c" /* yacc.c:1652  */
    break;

  case 34:
#line 112 "parser.y" /* yacc.c:1652  */
    { printf("ret ~\n\n"); }
#line 1559 "y.tab.c" /* yacc.c:1652  */
    break;

  case 35:
#line 113 "parser.y" /* yacc.c:1652  */
    { printf("ret\n\n"); }
#line 1565 "y.tab.c" /* yacc.c:1652  */
    break;

  case 36:
#line 117 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1571 "y.tab.c" /* yacc.c:1652  */
    break;

  case 37:
#line 118 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1577 "y.tab.c" /* yacc.c:1652  */
    break;

  case 38:
#line 122 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1583 "y.tab.c" /* yacc.c:1652  */
    break;

  case 39:
#line 126 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1589 "y.tab.c" /* yacc.c:1652  */
    break;

  case 40:
#line 130 "parser.y" /* yacc.c:1652  */
    { _BEG_IF; printf("_begIf_%d:\n", _i); }
#line 1595 "y.tab.c" /* yacc.c:1652  */
    break;

  case 41:
#line 134 "parser.y" /* yacc.c:1652  */
    { printf("\tjz _elIf_%d\n", _i); }
#line 1601 "y.tab.c" /* yacc.c:1652  */
    break;

  case 42:
#line 138 "parser.y" /* yacc.c:1652  */
    { printf("\tjmp _endIf_%d\n_elIf_%d:\n", _i, _i); }
#line 1607 "y.tab.c" /* yacc.c:1652  */
    break;

  case 43:
#line 142 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1613 "y.tab.c" /* yacc.c:1652  */
    break;

  case 44:
#line 146 "parser.y" /* yacc.c:1652  */
    { printf("_endIf_%d:\n\n", _i); _END_IF; }
#line 1619 "y.tab.c" /* yacc.c:1652  */
    break;

  case 45:
#line 150 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1625 "y.tab.c" /* yacc.c:1652  */
    break;

  case 46:
#line 154 "parser.y" /* yacc.c:1652  */
    { _BEG_WHILE; printf("_begWhile_%d:\n", _w); }
#line 1631 "y.tab.c" /* yacc.c:1652  */
    break;

  case 47:
#line 158 "parser.y" /* yacc.c:1652  */
    { printf("\tjz _endWhile_%d\n", _w); }
#line 1637 "y.tab.c" /* yacc.c:1652  */
    break;

  case 48:
#line 162 "parser.y" /* yacc.c:1652  */
    { printf("\tjmp _begWhile_%d\n_end_While_%d:\n\n", _w, _w); _END_WHILE; }
#line 1643 "y.tab.c" /* yacc.c:1652  */
    break;

  case 49:
#line 166 "parser.y" /* yacc.c:1652  */
    { printf("\tjmp _endWhile_%d\n", _w); }
#line 1649 "y.tab.c" /* yacc.c:1652  */
    break;

  case 50:
#line 170 "parser.y" /* yacc.c:1652  */
    { printf("\tjmp _begWhile_%d\n", _w); }
#line 1655 "y.tab.c" /* yacc.c:1652  */
    break;

  case 51:
#line 175 "parser.y" /* yacc.c:1652  */
    { printf("\tadd\n"); }
#line 1661 "y.tab.c" /* yacc.c:1652  */
    break;

  case 52:
#line 176 "parser.y" /* yacc.c:1652  */
    { printf("\tsub\n"); }
#line 1667 "y.tab.c" /* yacc.c:1652  */
    break;

  case 53:
#line 177 "parser.y" /* yacc.c:1652  */
    { printf("\tmul\n"); }
#line 1673 "y.tab.c" /* yacc.c:1652  */
    break;

  case 54:
#line 178 "parser.y" /* yacc.c:1652  */
    { printf("\tdiv\n"); }
#line 1679 "y.tab.c" /* yacc.c:1652  */
    break;

  case 55:
#line 179 "parser.y" /* yacc.c:1652  */
    { printf("\tmod\n"); }
#line 1685 "y.tab.c" /* yacc.c:1652  */
    break;

  case 56:
#line 180 "parser.y" /* yacc.c:1652  */
    { printf("\tcmpgt\n"); }
#line 1691 "y.tab.c" /* yacc.c:1652  */
    break;

  case 57:
#line 181 "parser.y" /* yacc.c:1652  */
    { printf("\tcmplt\n"); }
#line 1697 "y.tab.c" /* yacc.c:1652  */
    break;

  case 58:
#line 182 "parser.y" /* yacc.c:1652  */
    { printf("\tcmpge\n"); }
#line 1703 "y.tab.c" /* yacc.c:1652  */
    break;

  case 59:
#line 183 "parser.y" /* yacc.c:1652  */
    { printf("\tcmple\n"); }
#line 1709 "y.tab.c" /* yacc.c:1652  */
    break;

  case 60:
#line 184 "parser.y" /* yacc.c:1652  */
    { printf("\tcmpeq\n"); }
#line 1715 "y.tab.c" /* yacc.c:1652  */
    break;

  case 61:
#line 185 "parser.y" /* yacc.c:1652  */
    { printf("\tcmpne\n"); }
#line 1721 "y.tab.c" /* yacc.c:1652  */
    break;

  case 62:
#line 186 "parser.y" /* yacc.c:1652  */
    { printf("\tor\n"); }
#line 1727 "y.tab.c" /* yacc.c:1652  */
    break;

  case 63:
#line 187 "parser.y" /* yacc.c:1652  */
    { printf("\tand\n"); }
#line 1733 "y.tab.c" /* yacc.c:1652  */
    break;

  case 64:
#line 188 "parser.y" /* yacc.c:1652  */
    { printf("\tneg\n"); }
#line 1739 "y.tab.c" /* yacc.c:1652  */
    break;

  case 65:
#line 189 "parser.y" /* yacc.c:1652  */
    { printf("\tnot\n"); }
#line 1745 "y.tab.c" /* yacc.c:1652  */
    break;

  case 66:
#line 190 "parser.y" /* yacc.c:1652  */
    { printf("\tpush %s\n", yyvsp[0]); }
#line 1751 "y.tab.c" /* yacc.c:1652  */
    break;

  case 67:
#line 191 "parser.y" /* yacc.c:1652  */
    { printf("\tpush %s\n", yyvsp[0]); }
#line 1757 "y.tab.c" /* yacc.c:1652  */
    break;

  case 68:
#line 192 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1763 "y.tab.c" /* yacc.c:1652  */
    break;

  case 69:
#line 193 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1769 "y.tab.c" /* yacc.c:1652  */
    break;

  case 70:
#line 194 "parser.y" /* yacc.c:1652  */
    { /* empty */ }
#line 1775 "y.tab.c" /* yacc.c:1652  */
    break;

  case 71:
#line 198 "parser.y" /* yacc.c:1652  */
    { printf("\treadint %s\n", yyvsp[-1]); }
#line 1781 "y.tab.c" /* yacc.c:1652  */
    break;


#line 1785 "y.tab.c" /* yacc.c:1652  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;


#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif


/*-----------------------------------------------------.
| yyreturn -- parsing is finished, return the result.  |
`-----------------------------------------------------*/
yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 201 "parser.y" /* yacc.c:1918  */


int main() {
    return yyparse();
}