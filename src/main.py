import sys
import pandas as pd
import lexer

#arg 1 source code
#arg 2 reserved_words
#arg 3 scanning 
#arg 4 token_table
if __name__ == '__main__':
    # Users needs to enter right amount of arguments for personal test cases.
    if len(sys.argv) == 5:
        source_code = sys.argv[1]
        reserved_df = pd.read_csv(sys.argv[2])
        scanning_df = pd.read_csv(sys.argv[3])
        token_df = pd.read_csv(sys.argv[4])
    elif len(sys.argv) == 2:
        # If not, the provided test cases.
        source_code = sys.argv[1]
        reserved_df = pd.read_csv('../tables/reserved_words.csv')
        scanning_df = pd.read_csv('../tables/scanning_table.csv')
        token_df = pd.read_csv('../tables/token_table.csv')
    else:
        print(f"ERROR\n Expected 4 or 1 arguments. {len(sys.argv)-1} given.")
        exit(0)

    # Create lexer from the parse file.
    lex = lexer.LexicalAnalyzer(reserved_df,token_df,scanning_df,source_code)

    # Print the tokens for the user.
    for i in lex.parse_file():
        print(i)
    


