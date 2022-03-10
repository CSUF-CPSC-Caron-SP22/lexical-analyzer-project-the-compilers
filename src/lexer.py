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