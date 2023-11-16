import networkx as nx
import matplotlib.pyplot as plt
import re
G=nx.Graph()
R=nx.Graph()
P=nx.Graph()
F=nx.Graph()
nodes = [1, 2, 3, 4, 5, 6, 7, 8,9] # Здесь мы задаем по порядку номера всех существующих вершин
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (2, 3), (4,6),(6,2), (7,8),(5,9),(8,9)] # здесь мы задаем все связи между вершинами
G.add_nodes_from(nodes)
G.add_edges_from(edges)

degm=[val for (node, val) in G.degree()]
print(degm) # здесь мы выводим массив, где по порядку номеров вершин идут их степени
m1=[]
m2=[]
k=0
k1=[]
k2=[]
for i in range(len(edges)):
  k=str(edges[i])
  nums = re.findall(r'\d+', k)
  m1.append(int(nums[0]))
  k1.append(int(nums[0]))
  m2.append(int(nums[1]))
  k2.append(int(nums[1]))
# cоздание массивов со связями
cycle1=list(nx.find_cycle(G)) #поиск цикла
while True:
  k=0
  c2=str(cycle1)
  nums = re.findall(r'\d+', c2)
  nums = list(set(nums))
  for i in range(len(m1)):
    if (str(m1[i]) in nums) and (str(m2[i]) in nums):
      m1[i]=0
      m2[i]=0
      k+=1
  while 0 in m1: m1.remove(0)
  while 0 in m2: m2.remove(0)
  edges1=[]
  for i in range(len(m1)):
    x=(m1[i],m2[i])
    edges1.append(tuple(x))
  R.add_nodes_from(nodes)
  R.add_edges_from(edges1)
  cycle1=list(nx.find_cycle(R))
  if k==0:
    break
P.add_nodes_from(nodes)
P.add_edges_from(edges1)
degz=[val for (node, val) in P.degree()]
print(degz)
mx=[]
for i in range(len(degz)):
  if degz[i]==2:
    mx.append(i+1)
print(k1)
print(k2)
w1=[]
w2=[]
for i in range(len(mx)):
  for j in range(len(k1)):
    if k1[j]==mx[i]:
      w1.append(k2[j])
      w2.append(k1[j])
      k1[j]=0
      k2[j]=0
      break
    if k2[j]==mx[i]:
      w2.append(k1[j])
      w1.append(k2[j])
      k1[j]=0
      k2[j]=0
for i in range(len(w1)):
  if (w1[i] in mx):
    w1[i]=0
  if (w2[i] in mx):
    w2[i]=0
while 0 in k1: k1.remove(0)
while 0 in k2: k2.remove(0)
qwe=w1+w2
while 0 in qwe: qwe.remove(0)
print(qwe)
k1.append(qwe[0])
k2.append(qwe[1])
print(k1)
print(k2)
print(mx)
edges2=[]
for i in range(len(k1)):
  x=(k1[i],k2[i])
  edges2.append(tuple(x))
F.add_nodes_from(nodes)
F.add_edges_from(edges2)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
