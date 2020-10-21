from order_class import *
from functions import *

init_message()

order_1 = Order(user='Viru', adress='Juana Azurduy 1611', phone=45430869)

print(order_1)
while True:
    order_1.requested = input('Gusto cantidad:\n')
    if order_1.requested == '0':
        break
    if not valid_order(order_1.requested, valid_chara):
        print('Error, se debe ingresar un gusto y un numero separado por un espacio\n') 
        continue
  
    order_1.requested = order_1.parse_order()
    order_1.add_order()


if order_1.order_list:
    order_1.sort_order()
    order_1.show_list()
  
else:
    print('No ha hecho ningun pedido, será la próxima, Gracias!')