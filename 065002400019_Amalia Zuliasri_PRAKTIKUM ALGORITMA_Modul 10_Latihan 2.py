def bubble_sort_recursive(data, n=None):
    if n is None:  
        n = len(data)
    
    if n == 1:
        return

    for i in range(n - 1):
        if data[i] > data[i + 1]: 
            data[i], data[i + 1] = data[i + 1], data[i]
    
    bubble_sort_recursive(data, n - 1)

angka = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum Disorting:", angka)

bubble_sort_recursive(angka)
print("List Yang Sudah Disorting:", angka)


