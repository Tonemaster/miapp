lenguajes = ["Python","Csharp","PHP","GO","JAVA","Javascript"]
personas = [ [1,"Carlos",25],   [2,"Tomas",15], [3,"Mauricio",36]  ]

"""i = 1
while i<=10:
    print(i)
    i=i+1
    """

"""i=0
while i< len(lenguajes):
    print(lenguajes[i])
    i=i+1"""

"""for ddd in lenguajes:
    print(ddd)"""

for i in range(len(personas)):
    for j in range(len(personas[i])):
        print(personas[i][j])