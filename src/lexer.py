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
        index = 0

        while index < len(self.source_code):

            token = ''
            token_type = ""
            next_state = 0

            current_character = self.source_code[index]

            if current_character == "\n":
                current_character = "\\n"
                token += "\n"
            else:
                token += current_character

            # Check if the current character is in the columns names of the scanning table, else it is not a token.
            if current_character in list(self.scanning_table.columns.values):

                try:
                    try:
                        # next_state is the state of the token in scanning_table.
                        next_state = self.scanning_table[current_character][int(current_position)]  # (col, row)
                    except KeyError:
                        next_state = "<x>"
                    # If the next state is not empty then continue onto the next state.
                    while next_state != "<x>":
                        current_position = next_state
                        index += 1
                        current_character = self.source_code[index]

                                                
                        # if (current_character not in list(self.scanning_table.columns.values))
                        #     if current_position == 28  & (current_character != '*'):
                        #         next_row = 28
                        #     elif current_position == 18:
                        #         next_row = 18
                        #     elif current_position == 8:
                        #         next_row = 8
                        #     elif current_position == 8:
                        #         next_row = 8

                        # else:

                        try:
                            next_state = self.scanning_table[current_character][int(current_position)]  # (col, row)
                        except KeyError:
                            next_state = "<x>"

                        if next_state != "<x>":
                            token += current_character
                
                except:
                    token_type = "1 Error: invalid token"

            else:
                index += 1

            try:
                token_type = self.token_table[int(current_position)][0]
                if self.token_table[int(current_position)] == '<x>':
                    raise TypeError("Invalid token")

            except:
                token_type = "2 Error: invalid token"

            # Checking if identifier is a reserved word.
            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            # ToDo no_token_type error
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
