#Inicializar las variables
descripcionmujer = ''
descripcionhombre = ''
descripcioncamino = ''
nombremujer = ''
nombrehombre = ''
animal = ''
regalo = ''
respuesta = ''


#Preguntas especificas para las variables
nombremujer = input('Ingrese el nombre de ella:')
nombrehombre = input('Ingrese nombre de el:')
animal = input('Ingrese el nombre de su animal favorito:')
regalo = input('Ingrese el nombre de lo primero que vea al ir a un baño:')
descripcionmujer = input('Ingrese el nombre de una flor:')
descripcionhombre = input('Ingrese la marca de un auto:')
descripcioncamino = input('¿Qué tal eres bailando?:')
respuesta = input('¿Qué le dirías a alguien que te dio una vaca?')

#Mostrar la historia

print('Había una vez ')
print('Una chica llamada ' + nombremujer.capitalize() + '.')
print('Un día, ' + nombremujer.capitalize() + ' estaba caminando ' + descripcioncamino.lower() + ' por la calle ' + '.')
print("Y ella se fijo en un " + descripcionhombre.lower() + " llamado " + nombrehombre.capitalize() + ".")
print('El dijo: ¡Tu realmente eres una ' + descripcionmujer.lower() + '!' )
print("Ella dijo '" + respuesta.capitalize() + ", " + nombrehombre.capitalize() + ". '")
print("Ellos decicieron adoptar un " + animal.lower() + " y vivieron felices por siempre.")
