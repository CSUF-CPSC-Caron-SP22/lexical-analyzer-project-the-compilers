# Lexical Analyzer Project

-- ALL EQUAL WORKED ON THIS --

## The Compilers

#### Robert Pace (rpaceiv@csu.fullerton.edu)

    main.py (Pair Programming)
    preprocessor.py (Pair Programming)
    lexer.py (Pair Programming)
    DFA Diagram/Tables

#### Allen Rivas (allen.rrivas30@csu.fullerton.edu)

    main.py (Pair Programming)
    preprocessor.py (Pair Programming)
    lexer.py (Pair Programming)
    DFA Diagram/Tables

#### Jacob Ursenbach (jlursenbach@csu.fullerton.edu)

    main.py (Pair Programming)
    preprocessor.py (Pair Programming)
    lexer.py (Pair Programming)
    DFA Diagram/Tables

---

### Description

Created a table driven lexical analyzer for MiniC which uses a scanning table for the identification of tokens and to ignore comments which is written in Python.

---

### Installation and Usage

    Clone: 'git clone https://github.com/CSUF-CPSC-Caron-SP22/lexical-analyzer-project-the-compilers.git'
    Run: '$ make'

---

### Input and Output

    Input:

        int main() {

        float _id_a_t = 10.0E+4;
        float _id_a_t = 2.7;
        float result = _id_a_t + _id_b_t;
        result*=3;
        print(result);
        hey &
        int sum = 4+3

        math.sum(_id_a_t,_id_a_t);

        /* this is a \t multi 
        line comment */

        // This is & a \n single \r line comment.

        string a = "Hello I am a string.\n";


        }

    Output:

        ('int', 'int')
        ('0x20 (space)', ' ')
        ('identifier', 'main')
        ('leftParen', '(')
        ('rightParen', ')')
        ('0x20 (space)', ' ')
        ('leftBrace', '{')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('float', 'float')
        ('0x20 (space)', ' ')
        ('identifier', '_id_a_t')
        ('0x20 (space)', ' ')
        ('assignOp', '=')
        ('0x20 (space)', ' ')
        ('floatLiteral', '10.0E+4')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('float', 'float')
        ('0x20 (space)', ' ')
        ('identifier', '_id_a_t')
        ('0x20 (space)', ' ')
        ('assignOp', '=')
        ('0x20 (space)', ' ')
        ('floatLiteral', '2.7')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('float', 'float')
        ('0x20 (space)', ' ')
        ('identifier', 'result')
        ('0x20 (space)', ' ')
        ('assignOp', '=')
        ('0x20 (space)', ' ')
        ('identifier', '_id_a_t')
        ('0x20 (space)', ' ')
        ('addOp', '+')
        ('0x20 (space)', ' ')
        ('identifier', '_id_b_t')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('identifier', 'result')
        ('assignOp', '*=')
        ('intLiteral', '3')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('identifier', 'print')
        ('leftParen', '(')
        ('identifier', 'result')
        ('rightParen', ')')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('identifier', 'hey')
        ('0x20 (space)', ' ')
        ('Error: invalid token, found at line: 8', '&')
        ('0x0A (line feed)', '\n')
        ('int', 'int')
        ('0x20 (space)', ' ')
        ('identifier', 'sum')
        ('0x20 (space)', ' ')
        ('assignOp', '=')
        ('0x20 (space)', ' ')
        ('intLiteral', '4')
        ('addOp', '+')
        ('intLiteral', '3')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('identifier', 'math')
        ('floatLiteral', '.')
        ('identifier', 'sum')
        ('leftParen', '(')
        ('identifier', '_id_a_t')
        ('comma', ',')
        ('identifier', '_id_a_t')
        ('rightParen', ')')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('commentMulti', '/* this is a \\t multi \\nline comment */')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('commentSingle', '// This is & a \\n single \\r line comment.')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('identifier', 'string')
        ('0x20 (space)', ' ')
        ('identifier', 'a')
        ('0x20 (space)', ' ')
        ('assignOp', '=')
        ('0x20 (space)', ' ')
        ('string', '"Hello I am a string.\\n"')
        ('semicolon', ';')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('0x0A (line feed)', '\n')
        ('rightBrace', '}')
---