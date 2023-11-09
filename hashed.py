import hashlib

def hash_something(some):
    #Encodear algo en formato de bytes
    some_bytes =  some.encode('utf-8')

    #Utiliza la función SHA-256 para crear un objeto hash
    hash_obj = hashlib.sha256(some_bytes)

    #Obtener la representación hexadecimal del hash
    some_hash = hash_obj.hexdigest()

    return some_hash

something = input("Ingrese lo que sea que quiera crear un hash de él :")

hashed_something = hash_something(something)
print(f"representación en hash es:{hashed_something}")