
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND AS ASC AVG BETWEEN BY COMMA COUNT DELETE DESC DOT DOUBLE FROM IN INSERT INTEGER INTO LPAR MAX MIN NAME NOT OR ORDER RPAR SELECT SET SUM TEXT UPDATE VALUES WHEREquery : select\n            | update\n            | insert\n            | deleteupdate : UPDATE table SET column '=' expression\n                | UPDATE table SET column '=' expression WHERE conlist\n                insert : INSERT INTO table VALUES LPAR expressions RPAR\n                | INSERT INTO table LPAR columns RPAR VALUES LPAR expressions RPARdelete : DELETE FROM tables\n                | DELETE FROM tables WHERE conlist select : SELECT columns FROM tables WHERE conlist ORDER BY columns\n                | SELECT columns FROM tables WHERE conlist ORDER BY columns order_type\n                | SELECT columns FROM tables WHERE conlist\n                | SELECT columns FROM tables ORDER BY columns\n                | SELECT columns FROM tables ORDER BY columns order_type\n                | SELECT columns FROM tables\n                | SELECT expression\n                | SELECT expression FROM tablesorder_type : ASC\n                | DESC  columns : columns COMMA column\n                | column\n                 column :  '*'\n                | NAME\n                | NAME DOT NAME\n                 aggregate : SUM LPAR TEXT RPAR\n                    | AVG LPAR TEXT RPAR\n                    | MAX LPAR TEXT RPAR\n                    | MIN LPAR TEXT RPAR\n                    | COUNT LPAR TEXT RPAR tables : table\n            | tables COMMA table table : NAME\n            | NAME AS NAME\n             conlist : condition\n                | condition AND conlist\n                | condition OR conlist\n                | NAME BETWEEN number AND number\n                | NAME IN LPAR select RPAR\n                 texts : TEXT\n                value :  number\n                | aggregate\n                | texts   condition : column '>' value\n                  | column '<' value\n                  | column '=' value\n                  | column '>' column\n                  | column '<' column\n                  | column '=' column\n                    number : int\n                | double int : INTEGERdouble : DOUBLE expressions : expressions COMMA expression\n                | expression expression : expression '+' expression\n                   | expression '-' expression\n                   | expression '*' expression\n                   | expression '/' expression\n                   | value "
    
_lr_action_items = {'SELECT':([0,107,],[6,6,]),'UPDATE':([0,],[7,]),'INSERT':([0,],[8,]),'DELETE':([0,],[9,]),'$end':([1,2,3,4,5,11,12,13,14,15,16,17,18,19,20,22,27,28,30,49,50,51,52,53,54,55,56,57,58,65,72,73,74,75,76,80,81,84,85,87,99,101,104,105,108,109,110,111,112,113,115,116,117,118,123,125,126,127,128,],[0,-1,-2,-3,-4,-17,-22,-23,-60,-24,-41,-42,-43,-50,-51,-40,-52,-53,-33,-9,-31,-16,-21,-18,-56,-57,-58,-59,-25,-34,-26,-27,-28,-29,-30,-10,-35,-32,-13,-5,-14,-7,-36,-37,-47,-44,-48,-45,-49,-46,-15,-19,-20,-6,-11,-38,-39,-12,-8,]),'*':([6,11,14,16,17,18,19,20,22,27,28,34,46,54,55,56,57,67,68,70,72,73,74,75,76,86,87,89,91,92,95,96,97,100,114,119,],[13,38,-60,-41,-42,-43,-50,-51,-40,-52,-53,13,13,38,38,38,38,13,13,13,-26,-27,-28,-29,-30,13,38,38,13,13,13,13,13,13,13,38,]),'NAME':([6,7,31,32,33,34,35,40,46,47,67,68,69,70,86,91,92,95,96,97,100,114,],[15,30,30,30,30,15,30,58,15,65,15,82,30,82,15,82,82,15,15,15,82,15,]),'SUM':([6,36,37,38,39,77,78,95,96,97,102,120,],[21,21,21,21,21,21,21,21,21,21,21,21,]),'AVG':([6,36,37,38,39,77,78,95,96,97,102,120,],[23,23,23,23,23,23,23,23,23,23,23,23,]),'MAX':([6,36,37,38,39,77,78,95,96,97,102,120,],[24,24,24,24,24,24,24,24,24,24,24,24,]),'MIN':([6,36,37,38,39,77,78,95,96,97,102,120,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'COUNT':([6,36,37,38,39,77,78,95,96,97,102,120,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'TEXT':([6,36,37,38,39,41,42,43,44,45,77,78,95,96,97,102,120,],[22,22,22,22,22,59,60,61,62,63,22,22,22,22,22,22,22,]),'INTEGER':([6,36,37,38,39,77,78,93,95,96,97,102,120,121,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DOUBLE':([6,36,37,38,39,77,78,93,95,96,97,102,120,121,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'INTO':([8,],[31,]),'FROM':([9,10,11,12,13,14,15,16,17,18,19,20,22,27,28,52,54,55,56,57,58,72,73,74,75,76,],[32,33,35,-22,-23,-60,-24,-41,-42,-43,-50,-51,-40,-52,-53,-21,-56,-57,-58,-59,-25,-26,-27,-28,-29,-30,]),'COMMA':([10,12,13,14,15,16,17,18,19,20,22,27,28,30,49,50,51,52,53,54,55,56,57,58,65,72,73,74,75,76,79,84,88,89,99,119,123,124,],[34,-22,-23,-60,-24,-41,-42,-43,-50,-51,-40,-52,-53,-33,69,-31,69,-21,69,-56,-57,-58,-59,-25,-34,-26,-27,-28,-29,-30,34,-32,102,-55,34,-54,34,102,]),'RPAR':([11,12,13,14,15,16,17,18,19,20,22,27,28,30,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,72,73,74,75,76,79,81,84,85,88,89,99,104,105,108,109,110,111,112,113,115,116,117,119,122,123,124,125,126,127,],[-17,-22,-23,-60,-24,-41,-42,-43,-50,-51,-40,-52,-53,-33,-31,-16,-21,-18,-56,-57,-58,-59,-25,72,73,74,75,76,-34,-26,-27,-28,-29,-30,90,-35,-32,-13,101,-55,-14,-36,-37,-47,-44,-48,-45,-49,-46,-15,-19,-20,-54,126,-11,128,-38,-39,-12,]),'+':([11,14,16,17,18,19,20,22,27,28,54,55,56,57,72,73,74,75,76,87,89,119,],[36,-60,-41,-42,-43,-50,-51,-40,-52,-53,36,36,36,36,-26,-27,-28,-29,-30,36,36,36,]),'-':([11,14,16,17,18,19,20,22,27,28,54,55,56,57,72,73,74,75,76,87,89,119,],[37,-60,-41,-42,-43,-50,-51,-40,-52,-53,37,37,37,37,-26,-27,-28,-29,-30,37,37,37,]),'/':([11,14,16,17,18,19,20,22,27,28,54,55,56,57,72,73,74,75,76,87,89,119,],[39,-60,-41,-42,-43,-50,-51,-40,-52,-53,39,39,39,39,-26,-27,-28,-29,-30,39,39,39,]),'ASC':([12,13,15,52,58,99,123,],[-22,-23,-24,-21,-25,116,116,]),'DESC':([12,13,15,52,58,99,123,],[-22,-23,-24,-21,-25,117,117,]),'=':([13,15,58,64,82,83,],[-23,-24,-25,77,-24,97,]),'>':([13,58,82,83,],[-23,-25,-24,95,]),'<':([13,58,82,83,],[-23,-25,-24,96,]),'AND':([13,15,16,17,18,19,20,22,27,28,58,72,73,74,75,76,81,106,108,109,110,111,112,113,],[-23,-24,-41,-42,-43,-50,-51,-40,-52,-53,-25,-26,-27,-28,-29,-30,91,121,-47,-44,-48,-45,-49,-46,]),'OR':([13,15,16,17,18,19,20,22,27,28,58,72,73,74,75,76,81,108,109,110,111,112,113,],[-23,-24,-41,-42,-43,-50,-51,-40,-52,-53,-25,-26,-27,-28,-29,-30,92,-47,-44,-48,-45,-49,-46,]),'ORDER':([13,15,16,17,18,19,20,22,27,28,30,50,51,58,65,72,73,74,75,76,81,84,85,104,105,108,109,110,111,112,113,125,126,],[-23,-24,-41,-42,-43,-50,-51,-40,-52,-53,-33,-31,71,-25,-34,-26,-27,-28,-29,-30,-35,-32,98,-36,-37,-47,-44,-48,-45,-49,-46,-38,-39,]),'WHERE':([14,16,17,18,19,20,22,27,28,30,49,50,51,54,55,56,57,65,72,73,74,75,76,84,87,],[-60,-41,-42,-43,-50,-51,-40,-52,-53,-33,68,-31,70,-56,-57,-58,-59,-34,-26,-27,-28,-29,-30,-32,100,]),'DOT':([15,82,],[40,40,]),'LPAR':([21,23,24,25,26,30,48,65,66,94,103,],[41,42,43,44,45,-33,67,-34,78,107,120,]),'SET':([29,30,65,],[46,-33,-34,]),'VALUES':([30,48,65,90,],[-33,66,-34,103,]),'AS':([30,],[47,]),'BY':([71,98,],[86,114,]),'BETWEEN':([82,],[93,]),'IN':([82,],[94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,],[1,]),'select':([0,107,],[2,122,]),'update':([0,],[3,]),'insert':([0,],[4,]),'delete':([0,],[5,]),'columns':([6,67,86,114,],[10,79,99,123,]),'expression':([6,36,37,38,39,77,78,102,120,],[11,54,55,56,57,87,89,119,89,]),'column':([6,34,46,67,68,70,86,91,92,95,96,97,100,114,],[12,52,64,12,83,83,12,83,83,108,110,112,83,12,]),'value':([6,36,37,38,39,77,78,95,96,97,102,120,],[14,14,14,14,14,14,14,109,111,113,14,14,]),'number':([6,36,37,38,39,77,78,93,95,96,97,102,120,121,],[16,16,16,16,16,16,16,106,16,16,16,16,16,125,]),'aggregate':([6,36,37,38,39,77,78,95,96,97,102,120,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'texts':([6,36,37,38,39,77,78,95,96,97,102,120,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'int':([6,36,37,38,39,77,78,93,95,96,97,102,120,121,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'double':([6,36,37,38,39,77,78,93,95,96,97,102,120,121,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'table':([7,31,32,33,35,69,],[29,48,50,50,50,84,]),'tables':([32,33,35,],[49,51,53,]),'conlist':([68,70,91,92,100,],[80,85,104,105,118,]),'condition':([68,70,91,92,100,],[81,81,81,81,81,]),'expressions':([78,120,],[88,124,]),'order_type':([99,123,],[115,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> select','query',1,'p_query','main.py',235),
  ('query -> update','query',1,'p_query','main.py',236),
  ('query -> insert','query',1,'p_query','main.py',237),
  ('query -> delete','query',1,'p_query','main.py',238),
  ('update -> UPDATE table SET column = expression','update',6,'p_update','main.py',242),
  ('update -> UPDATE table SET column = expression WHERE conlist','update',8,'p_update','main.py',243),
  ('insert -> INSERT INTO table VALUES LPAR expressions RPAR','insert',7,'p_insert','main.py',256),
  ('insert -> INSERT INTO table LPAR columns RPAR VALUES LPAR expressions RPAR','insert',10,'p_insert','main.py',257),
  ('delete -> DELETE FROM tables','delete',3,'p_delete','main.py',272),
  ('delete -> DELETE FROM tables WHERE conlist','delete',5,'p_delete','main.py',273),
  ('select -> SELECT columns FROM tables WHERE conlist ORDER BY columns','select',9,'p_select','main.py',284),
  ('select -> SELECT columns FROM tables WHERE conlist ORDER BY columns order_type','select',10,'p_select','main.py',285),
  ('select -> SELECT columns FROM tables WHERE conlist','select',6,'p_select','main.py',286),
  ('select -> SELECT columns FROM tables ORDER BY columns','select',7,'p_select','main.py',287),
  ('select -> SELECT columns FROM tables ORDER BY columns order_type','select',8,'p_select','main.py',288),
  ('select -> SELECT columns FROM tables','select',4,'p_select','main.py',289),
  ('select -> SELECT expression','select',2,'p_select','main.py',290),
  ('select -> SELECT expression FROM tables','select',4,'p_select','main.py',291),
  ('order_type -> ASC','order_type',1,'p_order_type','main.py',323),
  ('order_type -> DESC','order_type',1,'p_order_type','main.py',324),
  ('columns -> columns COMMA column','columns',3,'p_columns','main.py',328),
  ('columns -> column','columns',1,'p_columns','main.py',329),
  ('column -> *','column',1,'p_column','main.py',342),
  ('column -> NAME','column',1,'p_column','main.py',343),
  ('column -> NAME DOT NAME','column',3,'p_column','main.py',344),
  ('aggregate -> SUM LPAR TEXT RPAR','aggregate',4,'p_aggregate','main.py',353),
  ('aggregate -> AVG LPAR TEXT RPAR','aggregate',4,'p_aggregate','main.py',354),
  ('aggregate -> MAX LPAR TEXT RPAR','aggregate',4,'p_aggregate','main.py',355),
  ('aggregate -> MIN LPAR TEXT RPAR','aggregate',4,'p_aggregate','main.py',356),
  ('aggregate -> COUNT LPAR TEXT RPAR','aggregate',4,'p_aggregate','main.py',357),
  ('tables -> table','tables',1,'p_tables','main.py',361),
  ('tables -> tables COMMA table','tables',3,'p_tables','main.py',362),
  ('table -> NAME','table',1,'p_table','main.py',375),
  ('table -> NAME AS NAME','table',3,'p_table','main.py',376),
  ('conlist -> condition','conlist',1,'p_conlist','main.py',382),
  ('conlist -> condition AND conlist','conlist',3,'p_conlist','main.py',383),
  ('conlist -> condition OR conlist','conlist',3,'p_conlist','main.py',384),
  ('conlist -> NAME BETWEEN number AND number','conlist',5,'p_conlist','main.py',385),
  ('conlist -> NAME IN LPAR select RPAR','conlist',5,'p_conlist','main.py',386),
  ('texts -> TEXT','texts',1,'p_texts','main.py',398),
  ('value -> number','value',1,'p_value','main.py',405),
  ('value -> aggregate','value',1,'p_value','main.py',406),
  ('value -> texts','value',1,'p_value','main.py',407),
  ('condition -> column > value','condition',3,'p_condition','main.py',418),
  ('condition -> column < value','condition',3,'p_condition','main.py',419),
  ('condition -> column = value','condition',3,'p_condition','main.py',420),
  ('condition -> column > column','condition',3,'p_condition','main.py',421),
  ('condition -> column < column','condition',3,'p_condition','main.py',422),
  ('condition -> column = column','condition',3,'p_condition','main.py',423),
  ('number -> int','number',1,'p_number','main.py',432),
  ('number -> double','number',1,'p_number','main.py',433),
  ('int -> INTEGER','int',1,'p_int','main.py',436),
  ('double -> DOUBLE','double',1,'p_double','main.py',441),
  ('expressions -> expressions COMMA expression','expressions',3,'p_expressions','main.py',445),
  ('expressions -> expression','expressions',1,'p_expressions','main.py',446),
  ('expression -> expression + expression','expression',3,'p_expression','main.py',458),
  ('expression -> expression - expression','expression',3,'p_expression','main.py',459),
  ('expression -> expression * expression','expression',3,'p_expression','main.py',460),
  ('expression -> expression / expression','expression',3,'p_expression','main.py',461),
  ('expression -> value','expression',1,'p_expression','main.py',462),
]
