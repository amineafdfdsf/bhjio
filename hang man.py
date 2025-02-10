
t = 0
word = ['n', 'a', 'b', 'i', 'l']
you = ['_'] *len(word)
print(""" Ｗｅｌｃｏｍｅ ｔｏ ｔｈｅ ｇａｍｅ ｏｆ ｔｈｅ ｈａｎｇｅｄ ｍａｎ
      
                                |         
                                O            There is a word you must know.
                               /|\           You have 10 attempts. 
                               / \           If you fail, you will die.
                                    
                             --------                                    """)

while True :
    c = input("so what is your later : ")
    if c in word:
        n_c = word.index(c)
        you[n_c] = c
        print(''.join(you))
    elif c not in word:
        print("no man is not her  try again !")


    t=t+1
    if word == you :
        print( """winneeeer !!!
                       
                  O          
                 /|\           
                 / \   """)
        break
    elif t == 10:
        print("""looser moooooot now
         -----
           |   |
               |
               |
               |
           O   |
        --------
                   """)
        break