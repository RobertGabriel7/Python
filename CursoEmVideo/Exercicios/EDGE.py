import pyautogui

'''Alterar para edge'''
pyautogui.hotkey("alt", "tab")

'''Para abrir uma nova aba'''
pyautogui.hotkey("ctrl", "t")

'''Para pesaquisar'''
contador = 1

pesquisa_array = [
    "Como tocar bateria",
    "Algoritmos de ordenação",
    "Receitas de comida italiana",
    "Aprender inglês online",
    "Programação orientada a objetos",
    "Destinos de viagem baratos",
    "Melhores filmes de ficção científica",
    "Técnicas de meditação para iniciantes",
    "Exercícios para fortalecer o núcleo",
    "Desenvolvimento de aplicativos móveis",
    "Dicas de fotografia",
    "História da civilização antiga",
    "Como cultivar plantas em apartamento",
    "Aprender a desenhar",
    "Novidades tecnológicas",
    "Tendências de moda",
    "Como fazer networking profissional",
    "Teoria musical básica",
    "Aprender a cozinhar comida japonesa",
    "Mercado de ações para iniciantes"
]


while(contador < 11):
    pyautogui.write(f"{pesquisa_array[contador]}")
    pyautogui.press("enter",interval= 5)
    pyautogui.hotkey("ctrl", "t")
    contador = contador + 1


