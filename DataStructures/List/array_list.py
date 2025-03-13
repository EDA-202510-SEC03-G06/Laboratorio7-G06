def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    #Agrega un elemento al inicio de la lista.
    #Inserta el elemento al inicio de la lista y actualiza el tamaño de la lista en 1.
     my_list['elements'] = [element] + my_list['elements']
     my_list['size'] += 1 
     return my_list
 
 
def add_last(my_list, element):
    #Agrega un elemento al final de la lista.
    #Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1.
    
     my_list['elements'].append(element)
     my_list['size'] += 1
     return my_list
 
 
def size(my_list):
    #Retorna el tamaño de la lista.
    
     return my_list['size']


def first_element(my_list):
    #Retorna el primer elemento de una lista no vacía.
    #Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error index out of range.
    # Esta función no elimina el elemento de la lista.
    
    if my_list['size'] == 0:
        return "IndexError: list index out of range"
    return my_list['elements'][0]


def sub_list(my_list, pos_i, num_elements):
     
    if pos_i < 1 or pos_i > my_list["size"]:
        raise IndexError("list index out of range")

    sublist = {
        "elements": my_list["elements"][pos_i - 1: pos_i - 1 + num_elements],
        "size": min(num_elements, my_list["size"] - (pos_i - 1))
    }
    return sublist

def iterator(lst):
   
    return [element for element in lst] 

def default_sort_criteria(element_1, element_2):
    
    if isinstance(element_1, dict) and isinstance(element_2, dict):
        return float(element_1.get("average_rating", 0)) < float(element_2.get("average_rating", 0))
    return element_1 < element_2


def selection_sort(my_list, sort_crit):
    
    n = my_list["size"]
    elements = my_list["elements"]

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if sort_crit(elements[j], elements[min_index]):
                min_index = j
                
        elements[i], elements[min_index] = elements[min_index], elements[i]

    return my_list

def insertion_sort(my_list, sort_crit):
    
    for i in range(1, my_list['size']):
        current_value = my_list['elements'][i]
        position = i
        
        
        while position > 0 and sort_crit(current_value, my_list['elements'][position - 1]):
            my_list['elements'][position] = my_list['elements'][position - 1]
            position -= 1
        
       
        my_list['elements'][position] = current_value
    
    return my_list

def shellSort(my_list, sort_crit):
    n = len(my_list)
    gap = n//2
    
    while gap > 0:
        for i in range(gap,n):
            temp = my_list[i]
            j = i
            while j >= gap and sort_crit(temp, my_list[j-gap]) < 0:
                my_list[j] = my_list[j -  gap]
                j -= gap
            my_list[j] = temp
        gap //= 2
    return my_list

def merge(my_list, l, m, r, sort_crit):
    elements = my_list["elements"]
    n1 = m - l + 1
    n2 = r - m
    L = elements[l:m + 1]
    R = elements[m + 1:r + 1]
    i = 0     
    j = 0     
    k = l    

    while i < n1 and j < n2:
        if sort_crit(L[i], R[j]) < 0:
            elements[k] = L[i]
            i += 1
        else:
            elements[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        elements[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        elements[k] = R[j]
        j += 1
        k += 1
    return my_list
        
def mergeSort(my_list, l, r, sort_crit):
    
    if l < r:
        m = l+(r-l)//2
        mergeSort(my_list, l, r, sort_crit)
        mergeSort(my_list, m + 1, r, sort_crit)
        merge(my_list, l, m, r, sort_crit)
    return my_list

def partition(my_list, low, high, sort_crit):
    elements = my_list["elements"]
    pivot = my_list[high]
    i = low - 1
    
    for j in range(low, high):
        if sort_crit(elements[j], pivot) < 0:
            i += 1
            elements[i],elements[j] = elements[j], elements[i]

    elements[i + 1],elements[high] = elements[high], elements[i + 1]
    return i + 1

def quickSort(my_list, low, high, sort_crit):
    if low < high:
        pi = partition(my_list, low, high, sort_crit)
        quickSort(my_list, low, pi - 1, sort_crit)
        quickSort(my_list, pi + 1, high, sort_crit)
    return my_list