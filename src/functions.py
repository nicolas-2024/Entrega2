import random
import string
from datetime import datetime

def filtro(textt):
    for cadena in textt:
        t=cadena.split()
        if(len(t) > 1 and t[1].lower()[0] in 'aeiou'):  #si hay 2 palabras and si la primera letra de la segunda palabra es vocal, cumple
            print(cadena)
 
""" 
  Ej2:Encuentre el título con más palabras 
""" 
def mayor(text):
    wordMax = ""
    max=-11
    for t in text:
        cont=0
        for word in t:
            cont+=1
        if cont > max:
            max=cont
            wordMax=t
    return(wordMax)
    
"""
  Ej3:imprima todas las reglas que la contengan.

"""
def reglamento(reglamentos):
    palabra=input("Ingrese una palabra")
#elimino espacios en blanco y separo las cadenas con /n
    reglas=reglamentos.strip().split("\n")
    reglasConEstaPalabra=[]
    for regla in reglas:
    #me aseguro que distinga entre Minusc y Mayusc
        if(palabra.lower()in regla.lower()):
            reglasConEstaPalabra.append(regla)
    if(reglasConEstaPalabra):
        for regla in reglasConEstaPalabra:
#imprime cada regla en la que aparezca esta palabra
            print(regla.strip())
    else:
        print("No se encontraron reglas que contengan la palabra clave.")   
        
        
""" 
 Ej4:  Validación de nombre de usuario:
"""          
      
def unNro(name):
    #verifico si hay numero
    return any(char.isdigit() for char in name)
             
def validar(name):
    if len(name) >= 5 and unNro(name) and any(char.isupper() for char in name) and name.isalnum(): #char.isupper() true si hay mayusc, isalnum true si son letras y num.
        return print("Nombre valido")
    else:
        return print("Nombre de usuario no cumple con los requisitos.")

"""
 Ej5: Clasificación de velocidad de reacción en un juego
"""

def clasificar(time):
    if(time < 200):
        print("Rapido")
    else:
        if(time >= 200) and (time <= 500):
            print("Normal")
        else: 
            print("Lento")

"""
 Ej6: Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
"entretenimiento", "música" y "charla".
"""

def menciones(descriptions):
    palabras_clave = ["música", "charla", "entretenimiento"]
    contador = {palabra: 0 for palabra in palabras_clave}

    for descripcion in descriptions:
        descripcion = descripcion.lower()
     #Agarro cada palabra
        palabras = descripcion.split()  
        # Contamos cuántas veces aparece cada palabra clave
        for palabra in palabras_clave:
            contador[palabra] += palabras.count(palabra)
    for palabra, cantidad in contador.items():
        print(f"Menciones de '{palabra}': {cantidad}")

"""
 Ej7: Genere un código de descuento aleatorio para un usuario en base a su nombre, la fecha
actual y el resto deben ser números o letras aleatorias:
"""

def generar(user,fecha):
    mayusc=user.upper()
    fecha = datetime.now().strftime('%Y%m%d')
    cod = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    print(f"Tu codigo es: {mayusc}-{fecha}-{cod}")
    
"""
 Ej8:si las listas son iguales, significa q tienen mismas letras y cantidad:
"""
def identificar(pri,seg):
    if(sorted(pri) == sorted(seg)):
        print("Son Anagrama")
    else:
        print("No son Anagramas")
        
"""
 Ej9:eliminar caracteres especiales y acentos:
"""
def Limpiar(clients):
    DatosLimpios = [] #Lista Pedida
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U'
    }
    sin_acentos=""
    for cliAct in clients:
        if cliAct is not None and cliAct != " " and cliAct != "":  #Si cliente actual != ..
            for letra in cliAct:
                if letra in acentos:
                    sin_acentos += acentos[letra]  # Quito acento
                else:
                    sin_acentos += letra  
            cliAct=sin_acentos
            esteDato = cliAct.strip().title()
            if esteDato not in DatosLimpios:
                DatosLimpios.append(esteDato)
            sin_acentos=""
    print("Lista limpia de clientes al realizar todas las operaciones:")
    return DatosLimpios