from random import *
import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import pandas as pd
import numpy as np
from prettytable import PrettyTable as pt

#задание 2
alfaArray=[]
gisto={0:0,1:0,2:0,3:0,4:0,5:0}
myTable = pt(["слой", "вершины"])
myTable2 = pt(["слой", "вершины"])
df=pd.DataFrame({'слой':[],
                                 'вершины':[]
                                 })
m=6
n=200

tree={1:0}
layer={1:0}

df.loc[1,'слой']='1'
df.loc[1,'вершины']=str(layer)

myTable.add_row(["1",str(layer)])


layer={}
currentIndex=1
g=randint(1,m-1)
futureLayer=[]
currentLayer=[]
countHangingNode=0;
for j in range(g):
    currentIndex+=1
    tree[currentIndex]=1
    layer[currentIndex]=1
    currentLayer.append(currentIndex)
df.loc[2,'слой']='2'
df.loc[2,'вершины']=str(layer)
myTable.add_row(["2",str(layer)])

layer={}
countLayer=3

hangingNode=[]

while(currentIndex-1<n):
    
    '''print(currentLayer)
    print(futureLayer)
    if len(currentLayer)==0:
        break;'''
    for i in range(len(currentLayer)):
        g=randint(0,m-1)
        if g == 0:
            countHangingNode+=1
            hangingNode.append(currentLayer[i])

        print(gisto)
        print(len(gisto))
        gisto[g]+=1
        for j in range(g):
            currentIndex+=1
            tree[currentIndex]=currentLayer[i]
            layer[currentIndex]=currentLayer[i]
            futureLayer.append(currentIndex)
    if len(futureLayer)!=0:
        currentLayer=futureLayer
        futureLayer=[]
    if len(hangingNode)!=0:
        myTable2.add_row([str(countLayer),str(hangingNode)])
    hangingNode=[]
    df.loc[countLayer,'слой']=str(countLayer)
    df.loc[countLayer,'вершины']=str(layer)
    myTable.add_row([str(countLayer),str(layer)])
    countLayer+=1
    layer={}
print(tree)
myTable2.add_row([str(countLayer),str(currentLayer)])
G=nx.Graph()
for k, v in tree.items():
    G.add_edge(k, v)
G.remove_edge(0,1)
G.remove_node(0)

plt.figure(1,figsize=(50,15)) 
pos = graphviz_layout(G, prog="dot")
nx.draw(G, pos, with_labels=True, arrows=False)
plt.show()

print(gisto)




#bar случайного
names = ['0', '1', '2','3','4', '5']
values=[]
for k, v in gisto.items():
    values.append(v)
print(values)
plt.figure(2)
plt.bar(names, values)
plt.show()




#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)
#df.style.set_properties(**{'text-align': 'left'})
#pd.reset_option('all')
print(df)



print("Все вершины")
print(myTable)



print("Висячие вершины")
print(myTable2)




#задание 3
#рабочий вариаент генерации фиксированного дерева с отображение bar графика распределения вершин

gisto={0:0,1:0,2:0,3:0,4:0,5:0}

m=6
n=200
tree={1:0}
currentIndex=1
g=5
futureLayer=[]
currentLayer=[]
countHangingNode=0;
for j in range(g):
    currentIndex+=1
    tree[currentIndex]=1
    currentLayer.append(currentIndex)

while(currentIndex-1<n):
    
    '''print(currentLayer)
    print(futureLayer)
    if len(currentLayer)==0:
        break;'''
    for i in range(len(currentLayer)):
        
        if g == 0:
            countHangingNode+=1
        gisto[g]+=1
        for j in range(g):
            currentIndex+=1
            tree[currentIndex]=currentLayer[i]
            futureLayer.append(currentIndex)
    if len(futureLayer)!=0:
        currentLayer=futureLayer
        futureLayer=[]
#print(tree)
#print(countList)

#отрисовка дерева
G=nx.Graph()
for k, v in tree.items():
    G.add_edge(k, v)
G.remove_edge(0,1)
G.remove_node(0)

plt.figure(1,figsize=(400,15)) 
pos = graphviz_layout(G,prog="dot")
nx.draw(G, pos, with_labels=True, arrows=False)
plt.show()


print(gisto)





#bar фиксированного
names = ['0', '1', '2','3','4','5']
values=[]
for k, v in gisto.items():
    values.append(v)
print(values)
plt.figure(3)
plt.bar(names, values)
plt.show()






#задание 4
#рабочий вариаент генерации случайного дерева с a
alfaArray=[]
countHangingNodeArray=[]
gisto={0:0,1:0,2:0,3:0,4:0,5:0}

m=6
n=200
tree={1:0}

for _ in range(100):
    currentIndex=1
    g=randint(1,m-1)
    futureLayer=[]
    currentLayer=[]
    countHangingNode=0;
    for j in range(g):
        currentIndex+=1
        tree[currentIndex]=1
        currentLayer.append(currentIndex)

    while(currentIndex-1<n):
        
        '''print(currentLayer)
        print(futureLayer)
        if len(currentLayer)==0:
            break;'''
        for i in range(len(currentLayer)):
            g=randint(0,m-1)
            if g == 0:
                countHangingNode+=1
            gisto[g]+=1
            for j in range(g):
                currentIndex+=1
                tree[currentIndex]=currentLayer[i]
                futureLayer.append(currentIndex)
                
        if len(futureLayer)!=0:
            currentLayer=futureLayer
            futureLayer=[]

    #print(tree)
    #print(countList)

    #отрисовка дерева
    '''G=nx.Graph()
    for k, v in tree.items():
        G.add_edge(k, v)
    G.remove_edge(0,1)
    G.remove_node(0)

    plt.figure(1,figsize=(35,15)) 
    pos = graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, arrows=False)
    plt.show()'''

    countHangingNode+=len(currentLayer)
    countHangingNodeArray.append(countHangingNode)
    alfaArray.append(currentIndex/countHangingNode)
print("Среднее значение висячих вершин")
print(sum(countHangingNodeArray)/len(countHangingNodeArray))
print("Среднее значение альфа")
print(sum(alfaArray)/len(alfaArray))









#задание 5
# рабочий вариаент генерации случайного дерева с отображением альфа от количества вершин
alfaArray=[0]
for col in range(400):
    m=3
    n=col
    tree={1:0}
    currentIndex=1
    g=randint(1,m-1)
    futureLayer=[]
    currentLayer=[]
    countHangingNode=0;
    for j in range(g):
        currentIndex+=1
        tree[currentIndex]=1
        currentLayer.append(currentIndex)

    while(currentIndex-1<n):
        
        '''print(currentLayer)
        print(futureLayer)
        if len(currentLayer)==0:
            break;'''
        for i in range(len(currentLayer)):
            g=randint(0,m-1)
            if g == 0:
                countHangingNode+=1
            for j in range(g):
                currentIndex+=1
                tree[currentIndex]=currentLayer[i]
                futureLayer.append(currentIndex)
        if len(futureLayer)!=0:
            currentLayer=futureLayer
            futureLayer=[]
    #print(tree)
    #print(countList)

#отрисовка дерева
    '''G=nx.Graph()
    for k, v in tree.items():
        G.add_edge(k, v)
    G.remove_edge(0,1)
    G.remove_node(0)

    plt.figure(1,figsize=(35,15)) 
    pos = graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, arrows=False)
    plt.show()'''
    
    countHangingNode+=len(currentLayer)

    alfaArray.append(currentIndex/countHangingNode)


#print(col)
print(alfaArray)
print("Среднее значение")
print(sum(alfaArray)/len(alfaArray))
#print(countHangingNode)
#print(currentIndex)







from networkx.drawing.nx_pylab import planar_layout
#график распределения a от количества вершин
plt.figure(4,figsize=(50,15))
a=plt.plot(alfaArray)
plt.rc('grid',linestyle=':',color='red',linewidth= 2)
plt.grid()
plt.show()

