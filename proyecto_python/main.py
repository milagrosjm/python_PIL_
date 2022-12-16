import tittles as t
import clases as c


def exists(array, value):
    bool = True if value < len(array) and value > -1 else False
    return bool

def itemInterface(index, projectIndex):
    while True:
        print("\n--------------------------------------------------------")
        print("\t\t\t" + projects[projectIndex].items[index].name)
        print("--------------------------------------------------------")
        print("Descripcion: " + projects[projectIndex].items[index].description)
        print ("Estado: " + projects[projectIndex].items[index].state)
        opt = int(input("\n1. Editar descripcion\n2. Cambiar estado\n3. Eliminar\n4. Volver\n\nIngresar opcion: "))
        if opt == 1:
            projects[projectIndex].items[index].description = input("\nNueva descripcion: ")
        elif opt == 2:
            itemState = int(input("\nIngrese nuevo estado (1. To Do - 2. In Progress - 3. Complete): "))
            projects[projectIndex].items[index].changeState(itemState)
        elif opt == 3:
            projects[projectIndex].deleteItem(projects[projectIndex].items[index])
            print("\n" + t.deleteditem)
            break
        elif opt == 4:
            break
        else:
            print("\n" + t.error + " - Opcion no valida")
       

def projectInterface(index):
    while True:
        print("\n--------------------------------------------------------")
        print("\t\t\t" + projects[index].name)
        print("--------------------------------------------------------\n")
        projects[index].listItems()
        opt = int(input("\n1. Agregar Item\n2. Seleccionar Item\n3. Mostrar items segun estado\n4. Eliminar Proyecto\n5. Volver\n\nIngresar opcion: "))
        if opt == 1:
            newItem(index)
        elif opt == 2:
            if len(projects[index].items) == 0:
                print("\n"+ t.error + " No hay items para seleccionar")
            else:
                itemIndex = int(input("\nIngrese el numero del Item: ")) - 1
                if exists(projects[index].items, itemIndex):
                    itemInterface(itemIndex, index)
                else: 
                    print("\n" + t.error +" - El valor ingresado es invalido")
        elif opt == 3:
            projects[index].listItemsByState()
        elif opt == 4:
            projects.remove(projects[index])
            print("\n"+t.deletedproject)
            break
        elif opt == 5:
            break
        else:
            print("\n" + t.error + " - Opcion no valida")


def listProjects():
    if len(projects) == 0:
        print(t.listTittle)
        print("\n¡Todavia no hay Proyectos!")
    else:
        while True:    
            print(t.listTittle + "\n")
            for p in projects:
                print("N°"+ str(projects.index(p) + 1) + " " +p.name)
            opt = int(input("\n1. Selecionar proyecto\n2. Volver\n\nIngrese una opcion: "))
            if opt == 1:
                projectindex = int(input("\nIngrese el numero del proyecto: ")) - 1
                if exists(projects, projectindex): 
                    projectInterface(projectindex)
                else: 
                    print("\n" + t.error +" - El valor ingresado es invalido")
            elif opt == 2:
                break
            else:
                print("\n" + t.error + " - Opcion no valida")


def newItem(index):
    tittle = input("\nTitulo: ")
    description = input("Descripcion: ")
    item = c.Item(tittle,description)
    projects[index].addItem(item)
    


def newProject():
    name = input("\nIngrese el nombre del proyecto: ")
    project = c.Project(name)
    projects.append(project)
    projectInterface(len(projects) - 1)
    

def menuMain():
    while True:
        print(t.pageName2)
        print("1. Crear nuevo Proyecto\n2. Ver Proyectos\n3. Salir")
        option = int(input("\nIngrese una opcion: "))
        if option == 1:
            newProject()
        elif option == 2:
            listProjects()
        elif option == 3:
            break
        else: 
            print("\n" + t.error + " - Opcion no valida")

def main():
    menuMain()
    

projects = []
if __name__=="__main__":
    main()