from cgitb import html
from pipes import Template
from django.template import Template,Context
from django.http import HttpResponse
import datetime

"""
se crea un contsructor para la clase Persona  para representar los datos de la persona 2 y hacer el ejemplo con POO
"""

class Persona(object):
    def __init__(self,nombre,apellido):

        self.nombre=nombre
        self.apellido=apellido


""" creacion de la primera vista se crea una funcion vista saludo()"""

def saludo(request):
    persona2=Persona("Miriam","Davila")
    nombre = "William"
    apellido = "Guillermo"
    ahora = now=datetime.datetime.now()
    doc_externo=open("/home/wguillermo/Escritorio/pildoras/proyecto1/proyecto1/saludo.html")
    plt = Template(doc_externo.read())
    doc_externo.close
    #ctx = Context({"nombre_persona":nombre,"nombre_apellido":apellido,"fecha_actual":ahora})
    ctx = Context({"nombre_persona":persona2.nombre,"nombre_apellido":persona2.apellido,"fecha_actual":ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse(" Hasta luego Django exit")

def fecha(request):
    """todas las funciones en la vista reciben un parametro request y devuelve un Http response,
    en la funcion fecha se importa el modulo datetime para imprimir en pantalla la fecha y hora actual
    """
    now=datetime.datetime.now()
    Documento = """<html>
    <body>
    <h1> La fecha actual es: now %s 
    </body>
    </html>""" % now
    return HttpResponse(Documento)

def edad_futura(request,edad,agnio):
    
    periodo = agnio-2022
    futura = edad+periodo
    documento="<html><body><h1> En el Año %s tendras %s</body></html>" %(agnio,futura)
    return HttpResponse(documento)


