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

import preprocessor as ppr
from typing import List
# import pandas as pd
# import numpy as np


class LexicalAnalyzer:

    def __init__(self, reserved_words_df, token_table_df, scanning_table_df,  source_code_file: str = ""):
        """"""
        self.PPR = ppr.Preprocessor(reserved_words_df, token_table_df, scanning_table_df, source_code_file)
        self.token_table = self.PPR.token_table
        self.scanning_table = self.PPR.scanning_table_df
        self.reserved_words = self.PPR.reserved_words
        self.source_code = self.PPR.source_code
        self.lexical_array = [('', '')]  # ("token_str","token_type")

    def parse_file(self, new_source: str = '') -> List[tuple]:
        """

        :param new_source:
        :return:
        """

        if new_source != '':
            self.PPR.set_file(new_source)

        current_position = 0

        for index in self.source_code:

            token = ''
            token_type = ""
            next_row = 0

            current_character = self.source_code[index]
            token += current_character

            try:
                next_row = self.scanning_table.loc[current_position, current_character]  # (row, col)

                while next_row != '':
                    index += 1
                    current_character = self.source_code[index]
                    next_row = self.scanning_table.loc[current_position, current_character]  # (row, col)

                    if next_row != '':
                        token += current_character
                        current_position = next_row

            except:
                token_type = "Error: invalid token"
                print(f"Error for token: |> {token} <| : not a valid token")
                token += current_character
                index += 1

                # ToDo error if token not found: Try/Catch might need to be reformatted
            try:
                token_type = self.token_table[current_position]
                if self.token_table[current_position] == '':
                    raise TypeError("Invalid token")
                # if error token_type = "error: no valid token"

            except:
                token_type = "Error: invalid token"
                print(f"Error for token: |> {token} <| : not a valid token")

            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            # ToDo no_token_type error

            self.lexical_array += (token, token_type)

        return self.lexical_array


"""
possible errors:

char does not match any inputs
    sets error as token type


"""


if __name__ == "__main__":

    LA = LexicalAnalyzer()
