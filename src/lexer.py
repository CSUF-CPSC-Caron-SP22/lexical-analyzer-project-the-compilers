import preprocessor as ppr
from typing import List

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

    def parse_file(self) -> List[tuple]:
        """
        The function is responsbile for choosing a token from the source code. Which, then it decides
        if the current state and current character should reach the goal, or not. 
        """

        # set initial variables

        # scanning table row
        current_position = 0
        # index of string
        index = 0
        # counter for code line number
        line_counter = 1

        # while iterating through source code
        while index < len(self.source_code):
            
            token = ''
            token_type = ""
            next_state = 0

            # character being investigated
            current_character = self.source_code[index]

            # .csv cannot hold pure /n, so change to match scanning table
            if current_character == "\n":
                line_counter += 1
                current_character = "\\n"
                token += "\n"
            else:
                # set token
                token += current_character
                
            # Check if the current character is in the columns names of the scanning table, else it is not a token.
            if current_character in list(self.scanning_table.columns.values):
                
                # if an error occurs, the token is invalid
                try:

                    # if the token is not in scanning table throw error
                    try:
                        # next_state is the state of the token in scanning_table.
                        next_state = self.scanning_table[current_character][int(current_position)]  # (row, col)
                    except KeyError:
                        next_state = "<x>"

                    # If the next state is not empty then continue onto the next state.
                    while next_state != "<x>":
                        # if index ==  len(self.source_code)-1:
                        #     break
                        current_position = next_state

                        # token was accepted, move to next token
                        index += 1
                        current_character = self.source_code[index]

                        # these characters need special working for .csv compatability
                        if current_character == "\n":
                            current_character = "\\n"
                        if current_character == "\t":
                            current_character = "\\t"                      
                        
                        # checks for unknown characters.
                        if current_character not in list(self.scanning_table.columns.values):

                            if int(current_position) == 28  and (current_character != '*'):
                                # multiline comments take all characters but end with *
                                next_state = 28
                            elif int(current_position) == 18:
                                # single line comments take all characters
                                next_state = 18
                            elif int(current_position) == 32:
                                # strings take all characters
                                next_state = 32
                            else:
                                # not a string, single line comment or multi line comment = not valid token
                                next_state = "<x>"
                        else:
                            # current character is in the scanning table
                            try:
                                # finds the cooresponding cell in scanning table
                                next_state = self.scanning_table[current_character][int(current_position)]  # (row, col)
                            except KeyError:
                                # if symbol not found in scanning table
                                if current_character == "\n":
                                    # control for multi line comments
                                    if int(current_position) == 28:
                                        next_state = 28
                                    else:
                                        # invalid token
                                        next_state = "<x>"

                        # not an end state (found a valid next step)
                        if next_state != "<x>":
                            token += current_character

                except:
                    token_type = "1 Error: invalid token"

            else:
                index += 1

            try:
                # set token type to cooresponding item in token table
                token_type = self.token_table[int(current_position)][0]
                # for a non-accepting state
                if self.token_table[int(current_position)][0] == '<x>':
                    raise TypeError("Invalid token")

            except:
                token_type = "Error: invalid token, found at line: " + str(line_counter)

            # Checking if identifier is a reserved word.
            if token_type == "identifier":
                for item in self.reserved_words:
                    if token == item:
                        token_type = item

            # adds token to lexical_array[]
            self.lexical_array.append((token_type,token))
            current_position = 0

        print("\nLexical analysis complete.",
                "\n(Token,Token Lexeme)")

        return self.lexical_array


# if __name__ == "__main__":

#     LA = LexicalAnalyzer()
