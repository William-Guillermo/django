from cgitb import html
from pipes import Template
from django.template import Template,Context
from django.http import HttpResponse
import datetime
from django.template import loader # modulo cargador de plantillas
from django.shortcuts import render

"""cargar
se crea un contsructor para la clase Persona  para representar los datos de la persona 2 y hacer el ejemplo con POO
"""

class Persona(object):
    def __init__(self,nombre,apellido):

        self.nombre=nombre
        self.apellido=apellido


""" creacion de la primera vista se crea una funcion vista saludo()"""

def saludo(request):
    persona2=Persona("Miriam","Davila")
    nombre = "William Guillermo"
    apellido = "De la Paz"
    temas=["Plantillas","vistas","modelos","BSE de datos","Apis","MVT"]
    # temas=[]
    ahora = now=datetime.datetime.now()
    # doc_externo=open("/home/wguillermo/Escritorio/pildoras/proyecto1/proyecto1/saludo.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close
    #doc_externo = loader.get_template('saludo.html')
    #ctx = Context({"nombre_persona":nombre,"nombre_apellido":apellido,"fecha_actual":ahora})
    #ctx = Context({"nombre_persona":persona2.nombre,"nombre_apellido":persona2.apellido,"fecha_actual":ahora,"clases":temas,"persona":nombre})
    #documento = doc_externo.render()
    return render(request,'saludo.html',{"nombre_persona":persona2.nombre,"nombre_apellido":persona2.apellido,"fecha_actual":ahora,"clases":temas,"persona":nombre})

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

def cursoC(request):

    now=datetime.datetime.now()
    return render(request,'cursoC.html',{'damefecha':now})

def cursojava(request):
    now=datetime.datetime.now()
    return render(request,'cursojava.html',{'damefecha':now})



