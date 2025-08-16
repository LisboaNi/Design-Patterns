from abc import ABCMeta, abstractmethod

# Abstract Factory
class pizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def add_pizza_veg(self):
        pass

    @abstractmethod
    def add_pizza(self):
        pass

# Concrete Factory A
class PizzaBr(pizzaFactory):

    def add_pizza_veg(self):
        return PizzaPalmito()
    
    def add_pizza(self):
        return PizzaCalabresa()

# Concrete Factory B
class PizzaItaliana(pizzaFactory):

    def add_pizza_veg(self):
        return PizzaMussarela()
    
    def add_pizza(self):
        return PizzaPepperoni()

# Abstract Product A

class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass

# Abstract Product B

class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass

# Product Concrete A1
class PizzaPalmito(PizzaVeg):

    def preparar(self):
        print(f"Preparando {type(self).__name__}")

# Product Concrete A2
class PizzaCalabresa(Pizza):

    def servir(self, PizzaVeg):
        print(f"{type(self).__name__} é servida com Calabresa na {type(PizzaVeg).__name__}")

# Product Concrete B1
class PizzaMussarela(PizzaVeg):
    
    def preparar(self):
        print(f"Preparando {type(self).__name__}")

# Product Concrete B2
class PizzaPepperoni(Pizza):

    def servir(self, PizzaVeg):
        print(f"{type(self).__name__} é servida com Pepperoni na {type(PizzaVeg).__name__}")

# Client 
class PizzaStore:

    def fazer_pizza(self):
        for fabrica in [PizzaBr(), PizzaItaliana()]:
            self.fabrica = fabrica
            self.pizza = self.fabrica.add_pizza()
            self.pizza_veg = self.fabrica.add_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)

pizzaria = PizzaStore()
pizzaria.fazer_pizza()