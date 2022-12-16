import tittles as t

class Item:

    def __init__(self, titulo, descripcion):
        self.name = titulo
        self.description = descripcion
        self.state = "Backlog"

    def changeState(self, number):
        if number == 1:
            self.state = "To Do"
        elif number == 2:
            self.state = "In Progress"
        else:
            self.state = "Complete"


class Project:

    def __init__(self, name): 
        self.name = name
        self.items = []    

    def listItems(self):
        if len(self.items) == 0:
            print("\n¡Todavia no hay Items!")
        else:
            print(t.items)
            for item in self.items:
                print("N°"+ str(self.items.index(item)+1)+" " + item.name)

    def listItemsByState(self):
        itemsBacklog = []
        itemsToDo = []
        itemsInProgress = []
        itemsComplete = []
        for item in self.items:
            if item.state == "Backlog":
                itemsBacklog.append(item)
            elif item.state == "To Do":
                itemsToDo.append(item)
            elif item.state == "In Progress":
                itemsInProgress.append(item)
            else: 
                itemsComplete.append(item)
        print("\nLos items en BACKLOG son: ")
        for i in itemsBacklog:
            print("-"+i.name)
        print("Los items PARA HACER son: ")
        for i in itemsToDo:
            print("-"+i.name)
        print("Los items EN PROGRESO son: ")
        for i in itemsInProgress:
            print("-"+i.name)
        print("Los items COMPLETADOS son: ")
        for i in itemsComplete:
            print("-"+i.name)
        #print("BACKLOG")
        #for i in itemsBacklog:
        #    print(item.name)
        #print("TO DO")
        #for i in itemsToDo:
        #    print(item.name)

    def addItem(self, item):
        self.items.append(item)

    def deleteItem(self, item):
        self.items.remove(item)

    