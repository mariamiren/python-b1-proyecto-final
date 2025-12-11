



"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/



        __init__.py
        food_package.py
        product.py



#product
class Product:
     def __init__(self, name: str, price: float, category: strs = ""): #inicializamos atributos creando nuevos objetos(name, price, category)
            self.name = name
            self.price = price
            self.category = category

         return f"Product(name='{self.name}', price='{self.price}', category='{self.category}')"



#food package
from products import Product
class FoodPackage

    def __init__(self):
        self.food_list = []
        
    def add_food(self, name: str, price: float): #crea y añade un producto de comida

        food= Product(name=name, price=rice, category="Food")
        self.food_list.append(food)
        
    def list_food(self): #muestra los productos de comida

        for f in self-food_list:
         print(f"{name}, {price}, Euro")
  



El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:



class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 


from products.food_package import SodaCup, BurgerWrap

cup = SodaCup()
wrap = BurguerWrap()

soda = Product(name = "Sprite", price = 2.0, category = "Bebida", package=  "cup")

burger = Product(name = "Hamburgesa", price = 12.50, category = "Comida", package = "wrap")
print(soda)
print(burger)

#empaques básicos
class SodaCup("Food.Package"):

    def pack(self)
        return "Vaso"
         
    def material(self)
        return "Cartón"
        
class BurgerWrap("Food.Package"):
    
    def pack(self):
        return "Envoltura"
        
    def material(self)
        return "Papel.Aluminio"

class Wrapping("Food.Package"):

    def pack(self):
        return "Envoltura"
        
    def material(self)
        return "Papel"

class Bottle("Food.Package"):

    def pack(self):
        return "Botella"
        
    def material(self)
        return "Plástico"

class Glass("Foodd.Package"):

    def pack(self)
        return "Vaso"
        
    def material(self)
        return "Vidrio"

class Box("Food.Package"):

    def pack(self):
        return "Caja"
        
    def material(self)
        return "Cartón"



El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:



class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()

from product import Product
from soda_cup import SodaCup
  
class Sprite(Product):
  
    def __init__(self):
        self.id = "G1"
        self.name = "Sprite"
        self.price = 5.0

    def type(self) -> str:
       return "Soda"
       
    def foodpackage(self):
       return SosaCup()
       
    def__str__(self)
    return f"{self.name}, {self.code}, {selfprice}"

   
from burger_warp import BurgerWrap

class BaconBurger(Product):

    def __init__(self):
         self.id = "H1"
         self.name = "BaconBurger"
         self.price = 15.0

    def type(self) -> str:
        return "Burguer"
       
    def Foodpackage(self):
       return BurguerWrap()
       
    def__str__(self):
    return f"{self.name} {self.code} - {selfprice}"


from products.drinks import get_drink_by_code(G1)
    
return(drink.name) # sprite
return(drink.foodpackage().pack()) #tipo


from product import Product
from happymeal import Happymeal
from soda import Sprite
from burger_bacon import BurguerBacon
  
class HappyMeal(Product):
    
    def __init__(self):
          self.code = M1
          self.name = "Happy Meal"
          self.price = 17.00

          self.drink = Sprite()
          self.burguer = BaconBurguer()
      
    def type(self)-> str:
          return "HappyMeal"
      
    def goodpackage(self):
          return HappyMeal()
      
    def cotents(self):
        return {
             "burguer": self.burguer
             "drink": self.drink
 }
    def __str__(self):
          return f" {self name}, {self.code}, {self price}




Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py


from users import User
class User():
 def__init (self, dni: str, name:str, age: int):
self.dni = dni
self.name = name
self.age = age

def describe(self) -> str:
#descripcion del usuario


from users import User
class Cashier(User):
  def __init__(self, dni: str, name: str, age: int)
  
  def describe(self) -> str:
      return f"Cajero{self.name}, {self.age}, {self.age}
      
  def process_order(self, order):
      return(f"{self.name}, {self.order}


        

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

class CSVFileManager:
    def __init__(self, folder_path: str):self.folder_path = folder_path
    
    def read(self, finlename: str->pd.Dataframe)
    #lee el archivo CSV y devuelvenData Frame
         filepath =
    os.path.join(self.folder_path, filename)
            if not os path.exists(filepath):
               raise
    FileNoFoundError
    df = pd.read_csv(filepath)
    return df

    def write(self, df: pd.DataFrame, filename: str):
    #convierte un dataframe en un archico csv
           filepath =
    os.path.join(self.folfer_path, filename)
    df.to_csv(filepath)
    return filepath


El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.


El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.


   import pandas as pd
import os

from typing import List

class converter:
       
    def convert(self, dataFrame, cls, *arg) -> List:
    #convierti cada fila de un dataframe en un objto clase, cls.
    cls= clase_destino("customer, cashier, baconburguer, sprite")
    *arg = atributos 
           
    objets = []
           
    obj = cls(*value)
    objects.append(obj)
    return objects
          
    def print(self, lista):
    #imprime informacion dfe la lista de objetos llamando__str__
     
         for item in lista:
             print(item)

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

class Order:

def __init__(self, cashier):
    Cashier, customer: (Customer)
    self.customer = Customer
    self.cashier = Cashier
    self.products = List[Product]
[]  #lista vacía

def add(self, product: Product): #agrega producto a la orden

def calculateTotal(self) -> float:
    total = 0.0
    for item in self.products:
        total += item.price
        return total

def show(self): #muestra informacion de la orden
    
print(f"Cashier:{self.cashier.name}")
print(f"Customer:{self.customer.name}")
for p in self.products:

print({p.name}, {p.price})
print total: {self.calculateTotal()}
        

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 

"""
#Write your code here

    
class PrepareOrder:

def __init__(self, cashier: Cashier, customer: Customer):
    self.cashier = cashier
    self.customer = customer
    self.order = Order(cashier, customer)
def add_prouct(self, product: Product):
    self.order.add(product) #agrega producto a la orden
def add_products_from_csv(self, csv_path:str, package_type= "Box"): #agrerfa productos a la orden desde un archivo CSV. CSV debe tener columnas; name, proce, category
    file_manager =
    CSVFileManager(csv_path)
df = file_manager.read()
converter = converter(df)
products = converter.to_product(package_type = package_type)

for p in products:
    self.orfder.add(p)
def show_order(self): # muestra la orden completa con todos los productos y empaques
    self.order.show()
        
 pass




