valid_chara = [
    'a', 'b', 'c', 'd', 
    'e', 'f', 'g', 'h', 
    'i', 'j', 'k', 'l', 
    'm', 'n', 'ñ', 'o', 
    'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 
    'x', 'y', 'z'
]


def init_message():
    print('''
    Bienvenide a "Empanadas de Python"
    Ingrese su pedido, escriba gusto y luego cantidad (ejemplo: "Carne 4")
    Para finalizar ingrese "0"
    Gustos sugeridos:
        - Carne  
        - Jamon y queso
        - Roquefort  
        - Pollo
        - Humita
        - Cebolla y queso
        - Panceta y ciruela
        - Verdura
        - Calabaza

    Si pide otra cosa le puede llegar cualquier porquería
    ''')


def valid_order(order, valid_chara):
    if len(order) < 7 or order[0].lower() not in valid_chara:
        return False
    else:
        return True