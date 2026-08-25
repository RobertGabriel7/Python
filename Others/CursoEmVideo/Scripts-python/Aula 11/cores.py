""" CORES NO TERMINAL PYTHON, FAMILIA """
""" 
>>>> STYLE <<<<

0 none      
1 Bold
4 Underline
7 Negative

>>>> TEXT (COR DO TEXTO) <<<<

30  Preto        
31  Vermelho 
32  Verde       
33  Amarelo 
34  Azul              
35  Magenta (roxo)
36  Ciano
37  Branco
39  Restaura a cor padrão

>>>> BACKGROUND (FUNDO)<<<<

40  Preto        
41  Vermelho 
42  Verde       
43  Amarelo 
44  Azul              
45  Magenta (roxo)
46  Ciano
47  Branco

# \ 033[STYLE: TEXT: BACKGROUNDm
\ 033[0:35:43m
 
para inverte
\ 033[7:30,
 
 
 """    
print('\033[1;34;40mFala Pessoal')
print('\033[4;37;40mTeste')

print('Testando cores \033[1;34;46m teste de cores')
print('Testando cores no python {} teste {}  '.format('\033[1;34;47m', '\033[m '))





