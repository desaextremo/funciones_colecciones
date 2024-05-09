def insertar_usuario(usuarios, usuario):
    """
    Inserta un nuevo usuario en el diccionario de usuarios.
    """
    nuevo_id = max(usuarios.keys()) + 1 if usuarios else 1
    usuario["id"] = nuevo_id
    usuarios[nuevo_id] = usuario

def eliminar_usuario(usuarios, usuario_id):
    """
    Elimina un usuario del diccionario de usuarios dado su ID.
    """
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        print(f"Usuario con ID {usuario_id} eliminado correctamente.")
    else:
        print(f"No se encontró ningún usuario con ID {usuario_id}.")

def buscar_usuario_por_id(usuarios, usuario_id):
    """
    Busca un usuario en el diccionario de usuarios dado su ID.
    """
    return usuarios.get(usuario_id)

def actualizar_usuario(usuarios, usuario_id, nueva_informacion):
    """
    Actualiza la información de un usuario en el diccionario de usuarios dado su ID.
    """
    if usuario_id in usuarios:
        usuario = usuarios[usuario_id]
        usuario.update(nueva_informacion)
        print(f"Información del usuario con ID {usuario_id} actualizada correctamente.")
    else:
        print(f"No se encontró ningún usuario con ID {usuario_id}.")

        
"""
Diccionario de usuarios, por el momento solo hay 1 usuario
"""
usuarios = {
    1: {
        "nombres": "Juan",
        "apellidos": "Pérez",
        "direccion": "Calle 123",
        "movil": "123456789",
        "email": "juan@example.com",
        "sexo": "M"
    },
    # Más usuarios...
}



# Insertar un nuevo usuario
nuevo_usuario = {
    "nombres": "María",
    "apellidos": "González",
    "direccion": "Avenida 456",
    "movil": "987654321",
    "email": "maria@example.com",
    "sexo": "F"
}
insertar_usuario(usuarios, nuevo_usuario)

# Eliminar un usuario
eliminar_usuario(usuarios, 1)

# Buscar un usuario por ID
usuario_encontrado = buscar_usuario_por_id(usuarios, 2)
print("Usuario encontrado:", usuario_encontrado)

# Actualizar la información de un usuario
actualizar_usuario(usuarios, 2, {"email": "maria.gonzalez@example.com"})
print("Usuario actualizado:", usuarios[2])