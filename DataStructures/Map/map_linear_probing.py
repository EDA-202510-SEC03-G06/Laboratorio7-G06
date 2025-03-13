def new_map(num_elements, load_factor, prime=109345121):
    """Crea una nueva tabla de símbolos con sondeo lineal."""
    capacity = nextprime(int(num_elements / load_factor))  
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
    """Calcula el valor de hash para la llave dada."""
    return (my_map['scale'] * hash(key) + my_map['shift']) % my_map['prime'] % my_map['capacity']

def find_slot(my_map, key):
    """Encuentra un espacio disponible usando sondeo lineal."""
    index = hash_value(my_map, key)
    capacity = my_map['capacity']
    
    for i in range(capacity):
        pos = (index + i) % capacity
        element = my_map['table']['elements'][pos]
        if element['key'] is None or element['key'] == key:
            return pos
    return None  


def put(my_map, key, value):
    """Agrega una nueva entrada llave-valor a la tabla de hash."""
    pos = find_slot(my_map, key)
    if pos is not None:
        if my_map['table']['elements'][pos]['key'] is None:
            my_map['size'] += 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
        my_map['table']['elements'][pos] = {'key': key, 'value': value}
    
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)
    
    return my_map

def contains(my_map, key):
    index = hash_value(my_map, key)
    while my_map['table']['elements'][index] is not None:
        if my_map['table']['elements'][index]['key'] == key:
            return True
        index = (index + 1) % my_map['capacity']
    return False
    
def get(my_map, key):
    """Obtiene el valor asociado a una llave dada."""
    index = _hash(my_map, key)
    while my_map['table']['elements'][index] is not None:
        if my_map['table'][index][0] == key:
            return my_map['table'][index][1]
        index = (index + 1) % my_map['capacity']
    return None

def remove(my_map, key):
    """Elimina una entrada de la tabla de símbolos."""
    index = _hash(my_map, key)
    while my_map['table'][index] is not None:
        if my_map['table'][index][0] == key:
            my_map['table'][index] = ('__EMPTY__', '__EMPTY__')
            my_map['size'] -= 1
            return my_map 
        index = (index + 1) % my_map['capacity']
    return my_map

def size(my_map):
    """Obtiene la cantidad de elementos en la tabla de símbolos."""
    return my_map['size']

def rehash(my_map):
    """Reajusta la tabla cuando se sobrepasa el factor de carga."""
    old_elements = [entry for entry in my_map['table']['elements'] if entry['key'] is not None]
    new_capacity = next_prime(my_map['capacity'] * 2)
    
    my_map['capacity'] = new_capacity
    my_map['table'] = {'size': new_capacity, 'elements': [{'key': None, 'value': None} for _ in range(new_capacity)]}
    my_map['size'] = 0
    my_map['current_factor'] = 0
    
    for entry in old_elements:
        put(my_map, entry['key'], entry['value'])
