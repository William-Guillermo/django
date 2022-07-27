from django.http import HttpResponse
import datetime


""" creacion de la primera vista se crea una funcion vista saludo()"""

def saludo(request):
    return HttpResponse("Primera pagina con Django")

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


