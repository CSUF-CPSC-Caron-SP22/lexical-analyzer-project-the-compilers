# from pandas import pd

class Preprocessor:
    def __init__(self,source_code_file,reserved_words_df,token_table_df,scanning_table_df):
        self.source_code = self.__fileToStr(source_code_file)
        self.reserved_words = self.__dFToList(reserved_words_df)
        self.token_table = self.__dFToDict(token_table_df)
        self.scanning_table_df = scanning_table_df

    '''This function takes in the source code and returns a string'''
    def __fileToStr(self, source_code_file) -> str:
        file = open(source_code_file, "r")
        return file.read()
    
    '''This function takes in a pandas data frame and returns a list'''
    def __dFToList(self,reserved_words_df) -> list:
        return reserved_words_df[reserved_words_df.columns[0]].tolist()

    '''This function takes in a pandas data frame and returns a dictonary'''
    def __dFToDict(self,token_table_df) -> dict:
        token_table = {}
        for row in token_table_df.itertuples():
                token_table[row[1]] = [row[2]]
        return token_table


#string code
#reserved list
#token table dict
#spanning dataframe