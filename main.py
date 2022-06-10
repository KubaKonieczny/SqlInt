import ply.lex as lex
import ply.yacc as yacc

from query_exec import Operations

op = Operations()
reserved = {
    'SELECT': 'SELECT',
    'UPDATE': 'UPDATE',
    'INSERT': 'INSERT',
    'INTO' : 'INTO',
    'DELETE': 'DELETE',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'ORDER': 'ORDER',
    'BY': 'BY',
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',
    'AVG': 'AVG',
    'BETWEEN': 'BETWEEN',
    'IN': 'IN',
    'SUM': 'SUM',
    'MAX': 'MAX',
    'MIN': 'MIN',
    'COUNT': 'COUNT',
    'AS': 'AS',
    'SET': 'SET',
    'VALUES': 'VALUES',
    'DESC': 'DESC',
    'ASC' : 'ASC'

}

# TOKENS
tokens = ['DOT', 'COMMA', 'LPAR', 'RPAR', 'INTEGER', 'DOUBLE', 'TEXT', 'NAME'] + list(reserved.values())

literals = ['+', '-', '*', '/', '=', '<', '>', '^']


# DEFINE TOKENS

def t_SELECT(t):
    r'[Ss][Ee][Le][Ee][Cc][Tt]'
    return t


def t_UPDATE(t):
    r'[Uu][Pp][Dd][Aa][Tt][Ee]'
    return t


def t_INSERT(t):
    r'[Ii][Nn][Ss][Ee][Rr][Tt]'
    return t


def t_DELETE(t):
    r'[Dd][Ee][Ll][Ee][Tt][Ee]'
    return t


def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'
    return t


def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    return t


def t_ORDER(t):
    r'[Oo][Rr][Dd][Ee][Rr]'
    return t


def t_BY(t):
    r'[Bb][Yy]'
    return t


def t_AND(t):
    r'[Aa][Nn][Dd]'
    return t


def t_OR(t):
    r'[Oo][Rr]'
    return t


def t_NOT(t):
    r'[Nn][Oo][Tt]'
    return t


def t_AVG(t):
    r'[Aa][Vv][Gg]'
    return t


def t_BETWEEN(t):
    r'[Bb][Ee][Tt][Ww][Ee][Ee][Nn]'
    return t

def t_INTO(t):
    r'[Ii][Nn][Tt][Oo]'
    return t


def t_IN(t):
    r'[Ii][Nn]'
    return t


def t_SUM(t):
    r'[Ss][Uu][Mm]'
    return t


def t_MAX(t):
    r'[Mm][Aa][Xx]'
    return t


def t_MIN(t):
    r'[Mm][Ii][Nn]'
    return t


def t_COUNT(t):
    r'[Cc][Oo][Uu][Nn][Tt]'
    return t

def t_ASC(t):
    r'[Aa][Ss][Cc]'
    return t
def t_DESC(t):
    r'[Dd][Ee][Ss][Cc]'
    return t
def t_AS(t):
    r'[Aa][Ss]'
    return t

def t_VALUES(t):
    r'[Vv][Aa][Ll][Uu][Ee][Ss]'
    return t


# def t_TEXT(t):
#     r'\'[[\w]+[\-]+[\w]+]+\'|\'[[\w\s]+[\-]+[\w\s]+]+\''
#     return t

# def t_TEXT(t):
#     r'.*'
#     return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    return t


def t_LPAR(t):
    r'\('
    return t


def t_RPAR(t):
    r'\)'
    return t


def t_COMMA(t):
    r'\,'
    return t


def t_DOT(t):
    r'\.'
    return t


# def t_PUNCTUATION(t):
#     r'\''
#     return t

def t_SET(t):
    r'[Ss][Ee][Tt]'
    return t

def t_NAME(t):
    r'[\w]+|[\w\s]+'
    return t

def t_TEXT(t):
    r'\'[\w-]+\'|\'[\w\s-]+\''
    return t


t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

lexer.lexliterals

data = '''SELECT a, b FROM literki AS l WHERE a > MAX(z) AND b = COUNT(a) ORDER BY a, b'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    #print(tok)


# PARSING

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/',)
)
def p_query(p):
    '''query : select
            | update
            | insert
            | delete'''


def p_update(p):
    '''update : UPDATE table SET column '=' expression
                | UPDATE table SET column '=' expression WHERE conlist
                '''
    t = p[2]
    c = p[4]
    e = p[6]
    w = None
    if len(p) == 9:
        w = p[8]

    op.query_exec("update", c, t, e, None, w)


def p_insert(p):
    '''insert : INSERT INTO table VALUES LPAR expressions RPAR
                | INSERT INTO table LPAR columns RPAR VALUES LPAR expressions RPAR'''

    t = p[3]
    c = None

    if len(p) == 8:
        e = p[6]
    else:
        e = p[9]
        c = p[5]

    op.query_exec("insert", c, t, e, None, None)


def p_delete(p):
    '''delete : DELETE FROM tables
                | DELETE FROM tables WHERE conlist'''

    t = p[3]
    w = None

    if len(p) == 6:
        w = p[5]

    op.query_exec("delete", None, t, None, None, w)

def p_select(p):
    ''' select : SELECT columns FROM tables WHERE conlist ORDER BY columns
                | SELECT columns FROM tables WHERE conlist ORDER BY columns order_type
                | SELECT columns FROM tables WHERE conlist
                | SELECT columns FROM tables ORDER BY columns
                | SELECT columns FROM tables ORDER BY columns order_type
                | SELECT columns FROM tables
                | SELECT expression
                | SELECT expression FROM tables'''

    c = None
    t = None
    o = None
    e = None
    w = None

    if len(p) == 11:
        w = p[6]
        o = [p[9], p[10]]
    elif len(p) == 10:
        w = p[6]
        o = [p[9], 'asc']
    elif len(p) == 9:
        o = [p[7], p[8]]
    elif len(p) == 8:
        o = [p[7], 'asc']
    elif len(p) == 7:
        w = p[6]


    if len(p) == 3:
        e = p[2]
    else:
        c = p[2]
        t = p[4]

    op.query_exec("select", c, t, e, o, w)


def p_order_type(p):
    '''order_type : ASC
                | DESC '''
    p[0] = p[1].lower()

def p_columns(p):
    ''' columns : columns COMMA column
                | column
                 '''
    col = []
    if len(p) == 2:
        col.append(p[1])
    elif len(p) == 4:
        for i in p[1]:
            col.append(i)
        col.append(p[3])
    p[0] = col


def p_column(p):
    '''column :  '*'
                | NAME
                | NAME DOT NAME
                '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[3]


def p_aggregate(p):
    ''' aggregate : SUM LPAR NAME RPAR
                    | AVG LPAR NAME RPAR
                    | MAX LPAR NAME RPAR
                    | MIN LPAR NAME RPAR
                    | COUNT LPAR NAME RPAR '''


def p_tables(p):
    '''tables : table
            | tables COMMA table'''

    col = []
    if len(p) == 2:
        col.append(p[1])
    elif len(p) == 4:
        for i in p[1]:
            col.append(i)
        col.append(p[3])
    p[0] = col


def p_table(p):
    ''' table : NAME
            | NAME AS NAME
            '''
    p[0] = p[1]


def p_conlist(p):
    ''' conlist : condition
                | condition AND conlist
                | condition OR conlist
                | NAME BETWEEN number AND number
                | NAME IN LPAR select RPAR
                 '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 or len(p) == 6:
        cond = []
        for c in p[1:]:
            cond.append(c)
        p[0] = cond


def p_texts(p):
    '''texts : TEXT
               '''

    p[0] = p[1][1:-1]


def p_value(p):
    ''' value :  number
                | aggregate
                | texts  '''
    if len(p) == 4:
        values = []
        for val in p[2]:
            values.append(val)
        p[0] = ' '.join(values)
    else:
        p[0] = p[1]


def p_condition(p):
    ''' condition : column '>' value
                  | column '<' value
                  | column '=' value
                  | column '>' column
                  | column '<' column
                  | column '=' column
                   '''
    cond = []
    for c in p[1:]:
        cond.append(c)

    p[0] = cond

def p_number(p):
    ''' number : int
                | double '''
    p[0] = p[1]
def p_int(p):
    '''int : INTEGER'''

    p[0] = int(p[1])

def p_double(p):
    '''double : DOUBLE'''
    p[0] = float(p[1])

def p_expressions(p):
    ''' expressions : expressions COMMA expression
                | expression'''
    expr = []
    if len(p) == 2:
        expr.append(p[1])
    elif len(p) == 4:
        for i in p[1]:
            expr.append(i)
        expr.append(p[3])
    p[0] = expr


def p_expression(p):
    ''' expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression
                   | LPAR expression RPAR
                   | value '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        else:
            p[0] = p[2]
def p_error(p):
    print("Syntax error in input!")

    # Build the parser


parser = yacc.yacc(debug=1)

#print(parser)
# parser.parse(data, debug=1)
# for x in parser.token()
# print(parser.token())
while True:
    try:
        s = input("Enter query or type 'help' or quit\n")
    except EOFError:
        break
    if not s:
        continue
    if s == 'q' or s == 'quit' :
        break
    elif s=='help' or s == '?':
        print('''
        SELECT kolumny FROM tabela [WHERE warunki] [ORDER BY kolumny [ASC|DESC]]
        SELECT wyrażenia_matematyczne
        UPDATE tabela SET kolumna = wartość [WHERE warunki]
        INSERT INTO tabela [(kolumny)] VALUES (kolumny)
        DELETE FROM table [WHERE warunek]''')
    else:
        result = parser.parse(s)

        print(result)
