def encontrarMinimoArreglo(arr):
	if arr[1] != 1:
		return 1

	if arr[-1] == len(arr) - 1:
		return len(arr)

	return encontrarMinimo(arr, 0, len(arr) - 1)


def encontrarMinimo(arreglo, start, end):
	if arreglo[0] < 0:
		arreglo[0] = 0
	primero = arreglo[0]
	if (start < end):
		mitad = int((start + end) / 2)
		if arreglo[mitad] != mitad + primero:
			return encontrarMinimo(arreglo, start, mitad)
		else:
			return encontrarMinimo(arreglo, mitad + 1, end)
	return start + primero


def main():
	numerosCant = int(input())
	numeros = list(map(int, input().split(" ")))
	numeros.sort()
	print(encontrarMinimoArreglo(numeros))


main()

