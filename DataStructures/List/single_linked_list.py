def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
        
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    #Agrega un elemento al inicio de la lista.
    #Agrega un nuevo nodo al inicio de la lista y aumenta el tamaño de la lista en 1.
    #En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    new_node = {'info': element, 'next': my_list['first']}
    
    if my_list['size'] == 0:
        my_list['last'] = new_node
    
    my_list['first'] = new_node
    my_list['size'] += 1
    
    return my_list

def add_last(my_list, element):
    #Agrega un elemento al final de la lista.
    #Agrega un nuevo nodo al final de la lista y aumenta el tamaño de la lista en 1.
    #En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    new_node = {'info': element, 'next': None}
    
    if my_list['size'] == 0:
        my_list['first'] = new_node
    else:
        my_list['last']['next'] = new_node
    
    my_list['last'] = new_node
    my_list['size'] += 1
    
    return my_list

def size(my_list):
    #Retorna el tamaño de la lista.
     return my_list['size']
 
def firs_element(my_list):
    #Retorna el primer elemento de una lista no vacía.
    #Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. 
    # Esta función no elimina el elemento de la lista.
    
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range')
    return my_list['first']['info']

def sub_list(my_list, pos_i, num_elements):
    """
    Retorna una sublista desde la posición `pos_i` con `num_elements` elementos.
    """
    if my_list["size"] == 0 or pos_i < 1 or pos_i > my_list["size"]:
        raise IndexError("Posición fuera de rango.")

    new_sublist = new_list()  
    current = my_list["first"]
    index = 1

    while current is not None and num_elements > 0:
        if index >= pos_i:
            add_last(new_sublist, current["info"])
            num_elements -= 1
        current = current["next"]
        index += 1

    return new_sublist

def iterator(lst):
   
    return [element for element in lst]

def selection_sort(my_list, sort_crit):
    
    if my_list["size"] < 2:
        return my_list  

    current = my_list["first"]

    while current is not None:
        min_node = current
        next_node = current["next"]

        while next_node is not None:
            if sort_crit(next_node["info"], min_node["info"]):
                min_node = next_node
            next_node = next_node["next"]

        current["info"], min_node["info"] = min_node["info"], current["info"]

        current = current["next"]

    return my_list

def default_sort_criteria(element_1, element_2):

    if isinstance(element_1, dict) and isinstance(element_2, dict):
        return float(element_1.get("average_rating", 0)) < float(element_2.get("average_rating", 0))
    return element_1 < element_2


def insertion_sort(my_list, sort_crit):
    
    if my_list["size"] < 2:
        return my_list  

    sorted_list = {"size": 0, "first": None}

    current = my_list["first"]

    while current is not None:
        new_node = {"info": current["info"], "next": None}

        if sorted_list["first"] is None or sort_crit(new_node["info"], sorted_list["first"]["info"]):
            new_node["next"] = sorted_list["first"]
            sorted_list["first"] = new_node
        else:
            prev = sorted_list["first"]
            while prev["next"] is not None and not sort_crit(new_node["info"], prev["next"]["info"]):
                prev = prev["next"]

            new_node["next"] = prev["next"]
            prev["next"] = new_node

        sorted_list["size"] += 1
        current = current["next"]

    return sorted_list

def get_node_at(my_list, pos):
    """Devuelve el nodo en la posición 'pos' (0-based)."""
    current = my_list["first"]
    index = 0
    while current and index < pos:
        current = current["next"]
        index += 1
    return current

def swap_nodes(node1, node2):
    """Intercambia los valores de dos nodos."""
    node1["info"], node2["info"] = node2["info"], node1["info"]

def shell_sort(my_list, sort_crit):
    """Ordena la lista enlazada usando Shell Sort."""
    n = my_list["size"]
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp_node = get_node_at(my_list, i)
            j = i

            while j >= gap and sort_crit(get_node_at(my_list, j - gap)["info"], temp_node["info"]) > 0:
                swap_nodes(get_node_at(my_list, j), get_node_at(my_list, j - gap))
                j -= gap

        gap //= 2

    return my_list

def merge_sort(my_list, sort_crit):
    """Ordena la lista enlazada usando Merge Sort."""
    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2
    left_list = sub_list(my_list, 1, mid)  # Corregido: inicio desde 1
    right_list = sub_list(my_list, mid + 1, my_list["size"] - mid)

    left_sorted = merge_sort(left_list, sort_crit)
    right_sorted = merge_sort(right_list, sort_crit)

    return merge(left_sorted, right_sorted, sort_crit)

def merge(left, right, sort_crit):
    """Fusiona dos listas enlazadas ordenadas en una sola lista enlazada ordenada."""
    merged_list = new_list()
    left_node = left["first"]
    right_node = right["first"]

    while left_node and right_node:
        if sort_crit(left_node["info"], right_node["info"]) <= 0:
            add_last(merged_list, left_node["info"])
            left_node = left_node["next"]
        else:
            add_last(merged_list, right_node["info"])
            right_node = right_node["next"]

    while left_node:
        add_last(merged_list, left_node["info"])
        left_node = left_node["next"]

    while right_node:
        add_last(merged_list, right_node["info"])
        right_node = right_node["next"]

    merged_list["size"] = left["size"] + right["size"]  # Corregido
    return merged_list

def get_previous(my_list, node):
    """Devuelve el nodo anterior a 'node' en la lista."""
    if my_list["first"] == node:
        return None  # No hay nodo previo si es el primero
    current = my_list["first"]
    while current and current["next"] != node:
        current = current["next"]
    return current

def partition(my_list, low, high, sort_crit):
    """Realiza la partición de la lista enlazada para QuickSort."""
    pivot = high["info"]
    i = low

    j = low
    while j is not high:
        if sort_crit(j["info"], pivot) < 0:
            i["info"], j["info"] = j["info"], i["info"]
            i = i["next"]
        j = j["next"]

    i["info"], high["info"] = high["info"], i["info"]
    return i

def quick_sort(my_list, low, high, sort_crit):
    """Ordena la lista enlazada usando QuickSort."""
    if low is not None and high is not None and low != high and low != high["next"]:
        pivot = partition(my_list, low, high, sort_crit)

        quick_sort(my_list, low, get_previous(my_list, pivot), sort_crit)
        quick_sort(my_list, pivot["next"], high, sort_crit)

    return my_list