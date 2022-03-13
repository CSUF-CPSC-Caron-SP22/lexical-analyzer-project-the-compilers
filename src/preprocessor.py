import pandas as pd

class Preprocessor:
    def __init__(self, reserved_words_df, token_table_df, scanning_table_df,  source_code_file: str = ""):
        self.source_code = self.__fileToStr(source_code_file)
        self.reserved_words = self.__dFToList(reserved_words_df)
        self.token_table = self.__dFToDict(token_table_df)
        self.scanning_table_df = scanning_table_df

    def __fileToStr(self, source_code_file: str = "") -> str:
        """
        This function takes in the source code and returns a string
        :param source_code_file:
        :return:
        """
        if source_code_file != '':
            file = open(source_code_file, "r")
            return file.read()
        else:
            return ""


    def __dFToList(self, reserved_words_df) -> list:
        """
        This function takes in a pandas data frame and returns a lis
        :param reserved_words_df:
        :return:
        """
        self.reserved_words = reserved_words_df[reserved_words_df.columns[0]].tolist()
        return self.reserved_words



    def __dFToDict(self, token_table_df) -> dict:
        """
        This function takes in a pandas data frame and returns a dictonary
        :param token_table_df:
        :return:
        """
        token_table = {}
        for row in token_table_df.itertuples():
            if row[1] in token_table:
                token_table[row[1]].append(row[2])
                print(row[1], row[2])
            else:
                token_table[row[1]] = [row[2]]

        self.token_table = token_table

        return self.token_table
