import pyparsing as pp
from pyparsing import Word, Literal, Combine, Group, Optional
from lark import Lark, Transformer

query_keywords = Word("Where", "Population", "Wage","State","Area","Rank")
operator = Literal("<") | Literal(">") | Literal("<=") | Literal("=>")|Literal("AND")|Literal("OR")|Literal("HELP")
expression = query_keywords + operator + query_keywords