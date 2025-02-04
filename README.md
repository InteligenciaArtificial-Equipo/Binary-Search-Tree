# Binary Search Tree with PY
## Explicación y Ejecución

## Team
### Chaparro Castillo Christopher
### Luis Antonio Peñuelas López

## Como Funciona?

## Clase Node

Tenemos la clase **Node**, la cual cuenta con los siguiente metodos:

- ### Inicializar

```py
def __init__(self, value):
  self.value = value
  self.left = None
  self.right = None
```
Recibe un valor para inicializar el valor del nodo, y los hijos como nulos.


- ### Insertar

```py
def insertNode(self, value):
  if value < self.value:
      if self.left is None:
          self.left = Node(value)
      else:
          self.left.insertNode(value)
  elif value >= self.value:
      if self.right is None:
          self.right = Node(value)
      else:
          self.right.insertNode(value)
```
Recibe el valor que se requiere insertar, se compara con el valor del nodo actual si es menor se se revisa si el no hay un hijo izquierdo si es asi se crea un nuevo Nodo y se inserta como hijo izquierdo caso contrario se llama recursivamente pero con el hijo izquierdo y se repite el procedimiento, de igual manera para cuando es mayor se sigue una logica muy similar.

- ### Buscar

```py
def search(self, value):
  if value < self.value:
      if self.left is None:
          return False
      return self.left.search(value)
  elif value > self.value:
      if self.right is None:
          return False
      return self.right.search(value)
  else:
      return True
```
Recibe el valor a buscar, se compara con el valor del Nodo actual si es menor se llama recursivamente el metodo search con el hijo izquierdo, si el valor es mayor se llamará al search con el hijo derecho, si es igual se retorna True ya que se ha encontrado, en caso de llegar a un valor None se retorna un False ya que el elemento no se encuentra contenido en el arbol.

- ### Print

```py
def printTree(self): #Inorder Traversal
  if self.left:
      self.left.printTree()
  print(self.value)
  if self.right:
      self.right.printTree()
```
Para imprimir el arbol se usa un recorrido Inorder que mostrara los elementos del arbol en orden creciente.

## Class BinarySearchTree

Tenemos una clase **BinarySearchTree** que se encarga más que nada de llamar los metodos del arbol usando la raiz

- ### Inicializar

```py
def __init__(self):
  self.root = None
```
Se inicializa un arbol con una raiz vacia.

- ### Insertar

```py
if self.root is None:
    self.root = Node(value)
else:
    self.root.insertNode(value)
```
Inserta el elemento si no hay una raiz coloca el elemento como raiz caso contrario llamara el metodo insert de la raiz del arbol.

- ### Buscar

```py
def search(self, value):
  if self.root is None:
      return False
  return self.root.search(value)
```
Si el arbol esta vacio retorna un False, caso contrario llamara el metodo search del nodo raiz.

- ### Print

```py
def printTree(self):
  if self.root is None:
      return
  self.root.printTree()
```
Si el arbol esta vacio return, caso contrario llamara el metodo print del nodo raiz e imprimira todo el arbol.

## Main

Agregamos un metodo main, para interactuar con el arbol y poder realizar las operaciones de manera dinamica.

```py
def main():
  bst = BinarySearchTree()
  
  while True:
      print("1. Insert")
      print("2. Search")
      print("3. Print")
      print("4. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
          value = int(input("Enter the value to insert: "))
          bst.insert(value)
      elif choice == 2:
          value = int(input("Enter the value to search: "))
          print("Value found" if bst.search(value) else "Value not found")
      elif choice == 3:
          print("Tree:")
          bst.printTree()
      elif choice == 4:
          break
      else:
          print("Invalid choice")
  print("Exiting...")
```

## Ejecuciones

### Ejecución 1

![Ejecucion1](https://github.com/user-attachments/assets/172df97a-dd8e-4b83-8bf2-f13e6546c707)

### Ejecución 2

![Ejecucion2](https://github.com/user-attachments/assets/c0e7c06d-aefb-4e8a-b236-e6ab8ee3c01b)
