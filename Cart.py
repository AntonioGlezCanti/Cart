import pandas as pd
import sys

class cart:

    def __init__(self):
        self.tabla = [] #tabla con los datos (tipo dataFrame)
        self.atDec = ""

    def _readCSV(self,ficheroCSV):
        self.tabla = pd.read_csv(ficheroCSV)
        self.atDec = self.tabla.columns[len(self.tabla.columns)-1]
        #print(self.tabla.iloc[0:3])

    def calcularRSS(self, j, at):
        s = self.tabla[at][j]
        r1 = self.tabla[self.tabla[at] < s]
        r2 = self.tabla[self.tabla[at] >= s]
        yR1 = r1[self.atDec].mean()
        yR2 = r2[self.atDec].mean()
        suma = 0
        for i in r1.index:
            suma += (r1[self.atDec][i] - yR1)**2
        for i in r2.index :
            suma += (r2[self.atDec][i] - yR2)**2
        return suma

    def calcularNodo(self):
        rssMin = sys.maxsize;
        atr = "";
        s = 0;
        verbose = "idx  Atr   Valor         RSS\n"
        for i in range(len(self.tabla.columns)-1):
            for j in range(len(self.tabla)):
                rss = self.calcularRSS(j,self.tabla.columns[i])
                if rss < rssMin:
                    rssMin = rss
                    atr = self.tabla.columns[i]
                    s = self.tabla[atr][j]
                verbose += f'{j}    {self.tabla.columns[i]}    {self.tabla[atr][j]}    {rss}\n'
        return rssMin, atr, s, verbose

tree = cart()
tree._readCSV(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv")
rss, atr, s, verbose = tree.calcularNodo()
print (f'rss: {rss}, atr: {atr}, s: {s}')
print(verbose)

#print(tree.calcularRSS(5,'x1'))