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
import pandas as pd
import numpy as np


class LexicalAnalyzer:

    def __init__(self, reserved_words_df, token_table_df, scanning_table_df,  source_code_file: str = ""):
        """"""
        self.PPR = ppr.Preprocessor(reserved_words_df, token_table_df, scanning_table_df, source_code_file)
        self.token_table = self.PPR.token_table
        self.scanning_table = self.PPR.scanning_table_df
        self.reserved_words = self.PPR.reserved_words
        self.source_code = self.PPR.source_code
        self.lexical_array = []  # ("token_str","token_type")

    def parse_file(self, new_source: str = '') -> List[tuple]:
        """

        :param new_source:
        :return:
        """

        # if new_source != '':
        ##    self.PPR.set_file(new_source)

        current_position = 0
        print(self.scanning_table['i'][0])
        print(f"token_table:{self.token_table}\n")

        print(self.token_table[8])
        index = 0

        while index < len(self.source_code):

            token = ''
            token_type = ""
            next_row = 0

            current_character = self.source_code[index]

            """while current_character == "\n":
                index += 1
                current_character = self.source_code[index]"""
            if current_character == "\n":
                current_character = "\\n"
                token += "\n"
            else:
                token += current_character


            try:

                print(f"------ \n"
                      f"     >Current position {current_position}\n"
                      f"     >Current character {current_character}")
                print(f"table found: {self.scanning_table[current_character][int(current_position)]}")
                try:
                    next_row = self.scanning_table[current_character][int(current_position)]  # (row, col)
                except KeyError:
                    print(f"error----------------1")
                    next_row = "<x>"

                print(f"next row:{next_row}")

                while next_row != "<x>":
                    current_position = next_row
                    print(f"pos: {current_position}")
                    index += 1
                    current_character = self.source_code[index]
                    print(f"char:{current_character}")
                    print(f"next_row= {current_character},{current_position}")
                    try:
                        next_row = self.scanning_table[current_character][int(current_position)]  # (row, col)
                    except KeyError:
                        print(f"error----------------2")
                        next_row = "<x>"

                    if next_row != "<x>":
                        print(f"next_row: {next_row}")
                        token += current_character

                    print(f"end-loop------------------\n")

            except:
                print(f"error----------------3")
                token_type = "1 Error: invalid token"
                print(f"Error for token: |> {token} <| : -----1------")

                # ToDo error if token not found: Try/Catch might need to be reformatted
            try:
                print(f"TOKEN INPUT current_position: {current_position}")
                token_type = self.token_table[int(current_position)][0]
                if self.token_table[int(current_position)] == '<x>':
                    raise TypeError("Invalid token")
                    # if error token_type = "error: no valid token"

            except:
                print(f"error----------------4")
                token_type = "2 Error: invalid token"
                print(f"Error for token: |> {token} <| : -----2-----")

            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            # ToDo no_token_type error
            print(f"TOKEN:{token},TOKEN_TYPE:{token_type}\n")
            self.lexical_array.append((token, token_type))
            current_position = 0

        return self.lexical_array



"""
possible errors:

char does not match any inputs
    sets error as token type


"""


if __name__ == "__main__":

    LA = LexicalAnalyzer()
