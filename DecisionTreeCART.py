import Cart
import numpy as np
import pandas as pd

class DecisionTreeCART :

    def __init__(self):
        self.tabla = []
        self.cart = None
    
    def learnDT(self,ficheroCSV,profMax,rama=None):
        self._readCSV(ficheroCSV)
        self.cart = Cart.Cart(self.tabla, profMax, rama)

    def _readCSV(self,ficheroCSV):
        self.tabla = pd.read_csv(ficheroCSV)
    
    def drawDecisionTree(self):
        return self.cart.pintarArbol(1,[])
    
    def verbose(self):
        return self.cart.verbose

    def prediction (self,registroCSV):
        registro = {}
        for i in range(len(registroCSV)):
            registro.update({self.tabla.columns.tolist()[i]:registroCSV[i]})
        print(self.cart.prediction(registro))


main = DecisionTreeCART()
main.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv", 2)
print(main.drawDecisionTree())
registro = [4, 6]
main.prediction(registro)

#rss, atr, s, verbose = tree.calcularNodo()
#print (f'rss: {rss}, atr: {atr}, s: {s}')
#print(verbose)
