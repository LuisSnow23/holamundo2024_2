from django.http import HttpResponse

# Create your views here.
def  vistaPaginaInicio(request):
     return HttpResponse('HolaMundo, Edmundo, Raymundo y Segismundo!')
