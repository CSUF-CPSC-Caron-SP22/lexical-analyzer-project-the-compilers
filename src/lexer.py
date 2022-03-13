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
    """
    Class is responsible for performing a lexical analysis.
    """
    def __init__(self, reserved_words_df, token_table_df, scanning_table_df,  source_code_file: str = ""):
        """
        Constructer which sets the token_table, scanning_table, reserved_words, and source_code, imported from the preprocessor.
        """
        self.PPR = ppr.Preprocessor(reserved_words_df, token_table_df, scanning_table_df, source_code_file)
        self.token_table = self.PPR.token_table
        self.scanning_table = self.PPR.scanning_table_df
        self.reserved_words = self.PPR.reserved_words
        self.source_code = self.PPR.source_code
        self.lexical_array = []  # ("token_str","token_type")

    def parse_file(self, new_source: str = '') -> List[tuple]:
        """
        The function is responsbile for choosing a token from the source code. Which, then it decides
        if the current state and current character should reach the goal, or not. 
        """

        current_position = 0
        print(self.scanning_table['i'][0])
        print(f"token_table:{self.token_table}\n")

        print(self.token_table[8])
        index = 0
        line_counter = 1
        while index < len(self.source_code):

            token = ''
            token_type = ""
            next_state = 0

            current_character = self.source_code[index]

            if current_character == "\n":
                line_counter += 1
                current_character = "\\n"
                token += "\n"
            else:
                token += current_character
            # Check if the current character is in the columns names of the scanning table, else it is not a token.
            if current_character in list(self.scanning_table.columns.values):

                try:

                    print(f"------ \n"
                          f"     >Current position {current_position}\n"
                          f"     >Current character {current_character}")
                    print(f"table found: {self.scanning_table[current_character][int(current_position)]}")
                    try:
                        # next_state is the state of the token in scanning_table.
                        next_state = self.scanning_table[current_character][int(current_position)]  # (row, col)
                    except KeyError:
                        print(f"error----------------1")
                        next_state = "<x>"

                    print(f"next row:{next_state}")
                    # If the next state is not empty then continue onto the next state.
                    while next_state != "<x>":
                        # if index ==  len(self.source_code)-1:
                        #     break
                        current_position = next_state
                        print(f"pos: {current_position}")
                        index += 1
                        current_character = self.source_code[index]
                        print(f"char:{current_character}")
                        print(f"next_state= {current_character},{current_position}")

                        if current_character == "\n":
                            current_character = "\\n"
                        if current_character == "\t":
                            current_character = "\\t"                      
                        if (current_character not in list(self.scanning_table.columns.values)):
                            if int(current_position) == 28  and (current_character != '*'):
                                next_state = 28
                            elif int(current_position) == 18:
                                next_state = 18
                            elif int(current_position) == 32:
                                next_state = 32
                            else:
                                next_state = "<x>"
                        else:
                            try:
                                next_state = self.scanning_table[current_character][int(current_position)]  # (row, col)
                            except KeyError:
                                print(f"KeyError----------------2")
                                if current_character == "\n":
                                    if int(current_position) == 28:
                                        next_state = 28
                                    else:
                                        next_state = "<x>"

                        if next_state != "<x>":
                            print(f"next_state: {next_state}")
                            token += current_character

                        print(f"end-loop------------------\n")

                except:
                    print(f"error----------------3")
                    token_type = "1 Error: invalid token"
                    print(f"Error for token: |> {token} <| : -----1------")

            else:
                index += 1

            try:
                print(f"TOKEN INPUT current_position: {current_position}")
                token_type = self.token_table[int(current_position)][0]
                if self.token_table[int(current_position)][0] == '<x>':
                    raise TypeError("Invalid token")

            except:
                print(f"error----------------4")
                token_type = "Error: invalid token, found at line: " + str(line_counter)
                print(f"Error for token: |> {token} <| : -----2-----")

            # Checking if identifier is a reserved word.
            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            # ToDo no_token_type error
            print(f"TOKEN:{token},TOKEN_TYPE:{token_type}\n")
            self.lexical_array.append((token_type,token))
            current_position = 0

        print("\nLexical analysis complete.",
                "\n(Token,Token Lexeme)")

        return self.lexical_array



"""
possible errors:

char does not match any inputs
    sets error as token type


"""


# if __name__ == "__main__":

#     LA = LexicalAnalyzer()
