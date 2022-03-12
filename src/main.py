import sys
import pandas as pd
# import preprocessor
import lexer

#argv 1 source code
#argv 2 reserved_words
#argv 3 scanning 
#argv 4 token_table

if __name__ == '__main__':
        
    if len(sys.argv) == 5:
        source_code = sys.argv[1]
        reserved_df = pd.read_csv(sys.argv[2])
        scanning_df = pd.read_csv(sys.argv[3])
        token_df = pd.read_csv(sys.argv[4])
    elif len(sys.argv) == 2:
        source_code = sys.argv[1]
        reserved_df = pd.read_csv('../tables/reserved_words.csv')
        scanning_df = pd.read_csv('../tables/scanning_table.csv')
        token_df = pd.read_csv('../tables/token_table.csv')
    else:
        print("ERROR")
        exit(0)

    lex = lexer.LexicalAnalyzer(reserved_df,token_df,scanning_df,source_code)

    print(lex.parse_file())
    # print(type(LEX.source_code))
    # print(type(LEX.reserved_words))
    # print(type(LEX.scanning_table_df))
    # print(type(LEX.token_table))

    # print('\n\n',LEX.source_code)
    # print('\n\n',LEX.reserved_words)
    # print('\n\n',LEX.scanning_table_df.head())
    # print('\n\n',LEX.token_table)
    


