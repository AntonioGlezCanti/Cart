import pandas as pd
import sys
import termcolor as tm

class Cart:

    def __init__(self, tabla, profMax, rama=None):
        self.tabla = tabla #tabla con los datos (tipo dataFrame)
        self.atDec = self.tabla.columns[len(self.tabla.columns)-1]
        self.hijos = {}
        self.atributo = None
        self.valor = None
        self.verbose = ""
        self.profMax = profMax
        self.rama = rama
        self.calcularNodo()

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
        if self.profMax == 0:
            self.nodo = self.tabla[self.atDec].mode()[0]
        elif self.tabla.empty:
            self.nodo = '?'
        elif self.tabla[self.atDec].mean() == 1 or self.tabla[self.atDec].mean() == 0:
            self.nodo = self.tabla[self.atDec].iloc[0]      
        else:
            rssMin = sys.maxsize;
            atr = "";
            s = 0;
            verbose = "idx  Atr   Valor         RSS\n"
            for i in range(len(self.tabla.columns)-1):
                for j in self.tabla.index:
                    rss = self.calcularRSS(j,self.tabla.columns[i])
                    if rss < rssMin:
                        rssMin = rss
                        atr = self.tabla.columns[i]
                        s = self.tabla[atr][j]
                    verbose += f'{j}    {self.tabla.columns[i]}    {self.tabla[atr][j]}    {rss}\n'
            self.atributo = atr
            self.valor = s
            self.nodo = f'{atr} < {s}'
            self.verbose = verbose
            self.crearHijos()
        
    def crearHijos(self):
        profR = self.profMax-1
        profL = self.profMax-1
        if self.rama == 'R':
            profL = 0; 
        elif self.rama == 'L':
            profR = 0;
        self.hijos.update({"Yes":Cart(self.tabla[self.tabla[self.atributo] < self.valor], profR)})    
        self.hijos.update({"No":Cart(self.tabla[self.tabla[self.atributo] >= self.valor], profL)})

    def prediction(self,registroCSV):
        if not bool(self.hijos):
            return self.nodo
        else:
            valor = registroCSV.get(self.atributo)
            if valor < self.valor:
                rama = "Yes"
            else:
                rama = "No"
            return self.hijos.get(rama).prediction(registroCSV)

    def pintarArbol(self, nvl, listNvl):
        s = tm.colored(f'{self.nodo}\n','red')
        if bool(self.hijos):
            numHijos = len(self.hijos)
            listNvl.append(nvl)
            for rama, nodo in self.hijos.items():
                numHijos-=1;
                tab = self.tabuladores(nvl,listNvl)
                s += tm.colored( tab + f'----{rama}\n','cyan')
                if numHijos == 0: listNvl.remove(nvl)
                tab = self.tabuladores(nvl+1,listNvl)
                s +=  tm.colored(tab + f'|----> {nodo.pintarArbol(nvl+2,listNvl)}','cyan')
        return s
    
    def tabuladores(self,nvl,listNvl):
        s = ""
        for i in range(1, nvl+1):
            s+='\t'
            if i in listNvl: s += '|'
        return s

#print(tree.calcularRSS(5,'x1'))