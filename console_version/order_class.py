class Order:
    def __init__(self, requested=None, oder_list=None, user=None, adress=None, phone=None):
        self.requested = requested
        self.order_list = oder_list
        self.user = user
        self.adress = adress
        self.phone = phone
        self.list_content()
  
    def list_content(self):
        if self.order_list is None:
            self.order_list = []


    def parse_order(self):
        self.aux_int = ''

        while True:
            if self.requested[-1] != ' ': 
                # esta bueno si de entrada haces order = order.strip() para asegurarte que si metio un espacio demas al final no rompa
                self.aux_int = self.requested[-1] + self.aux_int
                self.requested = self.requested.strip(self.requested[-1])
            else:
                self.requested = self.requested.strip(self.requested[-1])
                self.requested = [self.requested.capitalize(), int(self.aux_int)]
                return self.requested


    def add_order(self):
        for ix in range(len(self.order_list)):
            if self.order_list[ix][0] == self.requested[0]:
                self.order_list[ix][1] += self.requested[1]
                return self.order_list
        return self.order_list.append(self.requested)
  

    def sort_order(self):
        """ order_list[x][1] -> [1]=Value """
    
        for x in range(len(self.order_list)):
            for y in range(len(self.order_list)):
                if self.order_list[x][1] >= self.order_list[y][1]:
                    self.order_list[x], self.order_list[y] = self.order_list[y], self.order_list[x]


    def show_list(self):
        print('su pedido es:')
        for flavor in self.order_list:  
    # for flavor, amount in order_list queda mas legible para no usar indices despues
            if not flavor[1] == 0: 
                print('{} de {}'.format(flavor[1], flavor[0]))

    def __str__(self):
        return 'A nombre de: {}\nDirección: {}\nTeléfono: {}\nSu Pedido:\n{}'.format(
            self.user, self.adress, 
            self.phone, self.order_list
        )
