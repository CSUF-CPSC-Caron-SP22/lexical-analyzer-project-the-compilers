from parso import parse
from pandas import pd

class Preprocessor:
    def __init__(self,source_code_file,reserved_words_df,token_table_df,scanning_table_df):
        source_code = self.__fileToStr(source_code_file)
        reserved_words = self.__dFToList(reserved_words_df)
        token_table = self.__dFToDict(token_table_df)
        scanning_table_df = scanning_table_df

    def __fileToStr(self, source_code_file) -> str:
        file = open(source_code_file, "r")
        return file.read()
    
    def __dFToList(self,reserved_words_df) -> list:
        return reserved_words_df[reserved_words_df.columns[0]].tolist()
    
    def __dFToDict(self,token_table_df) -> dict:
        token_table = {}
        for row in token_table_df.itertuples():
            if row[1] in token_table:
                token_table[row[1]] = 
                print(row[1],row[2])
            else:
                token_table[row[1]] = []


#string code
#reserved list
#token table dict
#spanning dataframe