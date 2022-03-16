class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def obtenerNodoEnLaPosicionI(head: Node, i: int) -> Node:
    elNodoActual = head
    for _ in range(1, i):
        if elNodoActual == None:
            return None
        elSiguienteDelNodoActual = elNodoActual.next
        elNodoActual = elSiguienteDelNodoActual
    return elNodoActual


def insertarUnNodoEnLaPosicionI(head: Node, valor: int, i: int) -> Node:
    unNodoNuevo = Node(valor)
    if i == 1:
        unNodoNuevo.next = head
        head = unNodoNuevo
        return head
    elNodoEnLaPosicionIMenosUno = obtenerNodoEnLaPosicionI(head, i - 1)
    if elNodoEnLaPosicionIMenosUno == None:
        return head
    unNodoNuevo.next = elNodoEnLaPosicionIMenosUno.next
    elNodoEnLaPosicionIMenosUno.next = unNodoNuevo
    return head


def insertar(head: Node, valor, posI):
    return insertarUnNodoEnLaPosicionI(head, valor, posI)
