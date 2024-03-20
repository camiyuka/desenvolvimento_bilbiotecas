import random

nomes_de_animais = [
    "Garfield", "Miau", "Whiskers", "Luna", "Simba", "Frajola", "Nina", "Oliver", "Fofinho", "Branquinho", 
    "Pipoca", "Sombra", "Tom", "Bolinha", "Lili", "Sushi", "Marie", "Lilo", "Felix", "Mimi", "Salem", "Milo", 
    "Misty", "Nala", "Branquinha", "Sophie", "Cleo", "Coco", "Chico", "Toby", "Rex", "Bobby", "Bela", "Lobo", 
    "Daisy", "Duke", "Cindy", "Molly", "Bruno", "Dolly", "Charlie", "Buddy", "Lola", "Jake", "Lucy", "Bailey", 
    "Ziggy", "Sadie", "Teddy", "Ginger", "Zeus", "Roxy", "Ruby", "Marley", "Sky", "Kyo", "Hana", "Kaito", "Sakura", 
    "Tora", "Yuki", "Momo", "Sora", "Kiko", "Ren", "Haru", "Hoshi", "Neko", "Ichigo", "Mika", "Taro", "Sushi", "Kai", 
    "Kiko", "Kumi", "Yumi", "Ryu", "Akira", "Hikari", "Midori", "Mochi", "Yoshi", "Miyu", "Satsuki", "Hiro", "Suzu", 
    "Nobu", "Yua", "Toshi", "Sakana"
]

def gerar_nome_para_animais() -> str:
    return random.choice(nomes_de_animais)

def gerar_nome_para_animais_cli():
    print(random.choice(nomes_de_animais))
