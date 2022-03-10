'''

function lexer()
{
     repeat
           getchar();
           If input char terminates a token 
               AND it is an accepting state then
                   Isolate the token/lexeme
                   decrement the  CP if necessary
          else  lookup FSM (current state, input char);
     until (token found) or (no more input)
     
    If token found then
          return(token)    
 }
'''

import preprocessor.py as Preprocessor
from typing import List


class LexicalAnalyzer:

    def __init__(self, file, reserved_words, scanning_table, token_table):
        """"""
        preprocessor = Preprocessor.preprocessor
        token_table = Preprocessor.parse_token_table
        scanning_table = Preprocessor.parse_scanning_table
        reserved_words = Preprocessor.parse_reserved_words
        source_code = Preprocessor.parce_source_code

    def parse_file(self, code_list: list) -> List[tuple]:
        """

        :param code_list:
        :return:
        """

        lexical_array = [('', '')]

        for index in len(self.source_code):
            current_position = 0
            token = ''
            token_type = ''
            next_row = 0

            current_character = self.source_code[index]
            token += current_character
            next_row = self.scanning_table(current_character, current_position)

            while next_row != '':
                current_position = next_row
                index += 1
                current_character = self.source_code[index]
                next_row = self.scanning_table(current_character, current_position)

                if next_row != '':
                    token += current_character
                

                #ToDo error if token not found

            token_type = self.token_table[current_position]
                # if error token_type = "error: no valid token"

            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            #ToDo no_token_type error

            lexical_array += (token, token_type)

        return lexical_array


"""
possible errors:

char does not match any inputs
    sets error as token type
    
    
"""
