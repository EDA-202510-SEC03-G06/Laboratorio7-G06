from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Map.map_functions import next_prime
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    """Crea una nueva tabla de símbolos con sondeo lineal."""
    capacity = mf.next_prime(int(num_elements / load_factor))  
    scale = 1  
    shift = 0  
    table = [{'key': None, 'value': None} for _ in range(capacity)] 

    return {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': {'size': capacity, 'elements': table},
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0,
    }

def hash_value(my_map, key):
    """Calcula el índice de almacenamiento usando una función hash."""
    return (my_map['scale'] * hash(key) + my_map['shift']) % my_map['prime'] % my_map['capacity']


def find_slot(my_map, key, hash_value):
    """Encuentra un espacio disponible usando sondeo lineal."""
    index = hash_value
    capacity = my_map['capacity']
    
    for i in range(capacity):
        pos = (index + i) % capacity
        element = my_map['table']['elements'][pos]
        
        if element['key'] is None:
            return (False, pos)  
        if element['key'] == key:
            return (True, pos)  
    
    return (False, None)

def put(my_map, key, value):
    """Agrega una nueva entrada llave-valor a la tabla de hash."""
    hash_val = hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, hash_val)

    if pos is not None:
        if not occupied:  
            my_map['size'] += 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
        my_map['table']['elements'][pos] = {'key': key, 'value': value}
    
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)
    
    return my_map

def is_available(table, pos):
    """Verifica si una posición en la tabla está disponible."""
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def default_compare(key, entry):
    """Compara la llave key con la llave de una entrada dada."""
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def contains(my_map, key):
    """Verifica si la llave existe en la tabla."""
    index = hash_value(my_map, key)
    capacity = my_map['capacity']
    
    for i in range(capacity):
        pos = (index + i) % capacity
        element = my_map['table']['elements'][pos]
        if element['key'] == key:
            return True
        if element['key'] is None:
            return False
    return False

    
def get(my_map, key):
    """Obtiene el valor asociado a una llave dada."""
    index = hash_value(my_map, key)
    capacity = my_map['capacity']
    
    for i in range(capacity):
        pos = (index + i) % capacity
        element = my_map['table']['elements'][pos]
        if element['key'] == key:
            return element['value']
        if element['key'] is None:
            return None 
    return None


def remove(my_map, key):
    """Elimina una entrada de la tabla de símbolos."""
    hash_val = hash_value(my_map, key)
    occupied, pos = find_slot(my_map, key, hash_val)
    
    if occupied:
        my_map['table']['elements'][pos] = {'key': '__EMPTY__', 'value': '__EMPTY__'}
        my_map['size'] -= 1
    
    return my_map


def size(my_map):
    """Obtiene la cantidad de elementos en la tabla de símbolos."""
    return my_map['size']

def is_empty(my_map):
    """Valida si la tabla de símbolos está vacía."""
    return my_map['size'] == 0

def key_set(my_map):
    """Obtiene la lista de llaves de la tabla de símbolos."""
    keys = al.new_list()
    for entry in my_map['table']['elements']:
        if entry['key'] is not None and entry['key'] != '__EMPTY__':
            al.add_last(keys, entry['key'])
    return keys

def value_set(my_map):
    """Obtiene la lista de valores de la tabla de símbolos."""
    values = al.new_list()
    for entry in my_map['table']['elements']:
        if entry['key'] is not None and entry['key'] != '__EMPTY__':
            al.add_last(values, entry['value'])
    return values

def rehash(my_map):
    """Reajusta la tabla cuando se sobrepasa el factor de carga."""
    old_elements = [entry for entry in my_map['table']['elements'] if entry['key'] is not None]
    new_capacity = mf.next_prime(my_map['capacity'] * 2)  

    my_map['capacity'] = new_capacity
    my_map['table'] = {'size': new_capacity, 'elements': [{'key': None, 'value': None} for _ in range(new_capacity)]}
    my_map['size'] = 0
    my_map['current_factor'] = 0
    
    for entry in old_elements:
        put(my_map, entry['key'], entry['value'])

    return my_map
