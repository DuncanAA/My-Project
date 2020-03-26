class Pokemon:
    def __init__(self,name,weight,height,food,cp):
        self.__name=name
        self.__weight=weight
        self.__height=height
        self.__food=food
        self.__cp=cp
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_weight(self,weight):
        self.__weight=weight
    def get_weight(self):
        return self.__weight
    def set_height(self,height):
        self.__height=height
    def get_height(self):
        return self.__height
    def set_food(self,food):
        self.__food=food
    def get_food(self):
        return self.__food
    def set_cp(self,cp):
        self.__cp=cp
    def get_cp(self):
        return self.__cp
    def eat(self):
        print(f'The pokemon is eating{self.__food}.')
    def make_noice(self):
        print('The pokemon wow wow wow!')




class Pikachu(Pokemon):
    def __init__(self, name, weight, height, food, cp):
        super().__init__(name, weight, height, food, cp)
    def eat(self):
        print(f'{self.get_name()} is eating{self.get_food()}.pika')
    def make_noice(self):
        print(f'{self.get_name()} pika pika chu!')
