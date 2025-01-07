#Escritura
file = open('ejemplo.txt', 'a')
# 'a' --> escribe al final del archivo y si no existe, lo crea '''

for i in range(5):
    file.write(f'Hola mundo {i}, ')
file.write('Hola mundo 5.')
file.close()

#Lectura
file = open('ejemplo.txt', 'r')
lectura = file.read()
file.close()

#Imprimir en consola
print(lectura)