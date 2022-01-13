import DecisionTreeCART
import pandas as pd

""" Apartado a """
cart = DecisionTreeCART.DecisionTreeCART()
cart.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv", 1)
print("---Apartado a---")
print("arbol:")
print(cart.drawDecisionTree())
print("Verbose: ")
print(cart.verbose())

""" Apartado b """
t1 = DecisionTreeCART.DecisionTreeCART()
t1.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv", 2, "R")
t2 = DecisionTreeCART.DecisionTreeCART()
t2.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv", 2, "L")
print("---Apartado b---")
print("arbol 1:")
print(t1.drawDecisionTree())
print("arbol 2:")
print(t2.drawDecisionTree())

registrosCSV = pd.read_csv(r"C:\Users\gonza\Documents\Informática\Aprendizaje\Práctica CART\Cart\ejemplo.csv")
aciertost1 = 0
aciertost2 = 0
total = len(registrosCSV)
for i in registrosCSV.index:
    fila = registrosCSV.iloc[i].tolist()
    z = fila[len(fila)-1]
    res = t1.prediction(fila)
    if res == z:
        aciertost1 += 1
    res = t2.prediction(fila)
    if res == z:
        aciertost2 += 1
print(f'Accuracy del arbol T1: {aciertost1/total * 100}')
print(f'Accuracy del arbol T1: {aciertost2/total * 100}')