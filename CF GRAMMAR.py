# citim din fisier si introducem informatiile intr un dictionar format din cheia care va reprezenta simbolul neterminal si
#si valoarea care va reprezenta productia
file = open("grammar.txt")
fileLine = file.readline()
P = {}
symbol_to_start=''
while  fileLine!="":
    fileLine.strip()
    fileLine = fileLine.split("->")
    non_terminal = fileLine[0]

#pastram intr o variabila simbolul de start
    if  symbol_to_start=='':
        symbol_to_start = fileLine[0]

#adaugam vaorile in dictionar
    new = fileLine[1]
    new = new.strip().split("|")
    if non_terminal not in P:
        P[non_terminal] = []
        for element in new:
                P[non_terminal].append(element)
    fileLine = file.readline()
print(P)

#de aici incepem verificarea

def check_grammar(grammar, start_symbol, word):
    print(start_symbol)
    if len(word) == 0 : #verificam pentru cuvantul vid
        if start_symbol in grammar:
            for aux in grammar[start_symbol]:
                if aux[0]=='l':
                    return True
    else:
        #verificam daca exista in dictionar cheia corespunzatoarea simbolului de start
        if start_symbol in grammar:
            for aux in grammar[start_symbol]:
                #parcurgem lista corespunzatoare simbolului de start
                if word[0]==aux[0]:
                    #verific daca prima litera din cuvantul dat este egala cu simbolul neterminal din elementul listei parcurse
                    if len(word)==1:
                        #daca a intrat in in ul de mai sus si are si lungimea 1 , e clar ca se accepta cuvantul
                        return True
                    elif check_grammar(grammar,aux[1],word[1:]):
                        return True

word = input ()
rezultat = check_grammar(P,symbol_to_start,word);

if (rezultat ):
    print ("Cuvantul este acceptat!")
else:
    print("Cuvantul nu este acceptat!")



