from django.shortcuts import render
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xmlparser import myContentHandler
from xmlparser import myContentHandler
import urllib2
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from models import Hotel, PaginaUsuario, HotelesUsuario, Imagen, Comentario 
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def perfiles(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/')

def principal(request):

    respuesta=""
    salida=""
    lista=Hotel.objects.all()
    listauser=PaginaUsuario.objects.all()

    if len(lista) == 0:
        print("Parseando...")
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        fil = urllib2.urlopen("http://cursosweb.github.io/etc/alojamientos_es.xml")
        theParser.parse(fil)

    context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.user.is_authenticated():
        us=PaginaUsuario.objects.get(user=request.user.username)
        context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':"",'color':us.color,'size':us.size}

    return render_to_response('principal.html', context, context_instance = RequestContext(request))	

def nana(request):
    return HttpResponse("No se ha encontrado este idioma para este hotel")	

def alojamiento_id_frances(reuqest,id):
    fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_fr.xml')
    tree = ET.parse(fil)
    root = tree.getroot()
    hotel=Hotel.objects.get(id=id)

    encontrado = False
    for child in root.iter('basicData'):
        name=child.find('name').text
        if name == hotel.name:
                print name
                encontrado=True;
                body=child.find('body').text
                phone=child.find('phone').text
                web=child.find('web').text
                if body == None:
                    body="Info no disponible"
                if phone == None:
                    phone= "Telefono no disponible"
                if web == None:
                    web= " Web no disponible"
                break;
    if not encontrado:
        return HttpResponse(" Hotel no disponible en este idioma")
    for child in root.iter('geoData'):
        address=child.find('address').text
        if address==hotel.address:
            country=child.find('country').text
            break;
    for child in root.iter('media'):
        url=child.find('url').text

        if url == hotel.source:
            break;
    if url == None:
        url= " imagen nos disponible"
    return HttpResponse("<h1>"+name+"</h1>"+body+phone+"<br>" +"<a href="+web+">"+web+"</a>"+"</br>"+address+"</br>"+country+"</br><img src="+url+"></img>")





def alojamiento_id_ingles(reuqest,id):
    encontrado=False;
    fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_en.xml')
    tree = ET.parse(fil)
    root = tree.getroot()
    hotel=Hotel.objects.get(id=id)
    print hotel.name
    for child in root.iter('basicData'):
        name=child.find('name').text

        if name == hotel.name:
                encontrado=True;
                body=child.find('body').text
                phone=child.find('phone').text
                web=child.find('web').text
                if body == None:
                    body="Info no disponible"
                if phone == None:
                    phone= "Telefono no disponible"
                if web == None:
                    web= " Web no disponible"
                break;
    if not encontrado:
        return HttpResponse(" Hotel no disponible en este idioma")
    for child in root.iter('geoData'):
        address=child.find('address').text
        if address==hotel.address:
            country=child.find('country').text
            break;
    for child in root.iter('media'):
        url=child.find('url').text

        if url == hotel.source:
            print url
            break;

    return HttpResponse("<h1>"+name+"</h1>"+body+phone+"<br>" +"<a href="+web+">"+web+"</a>"+"</br>"+address+"</br>"+country+"</br><img src="+url+"></img>")




def alojamientos(request):
    lista=Hotel.objects.all()
    listauser=PaginaUsuario.objects.all()
    context = {'lista':lista,'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.method =='POST':
        valuetype = request.POST.get('filtrotipo', "")
        valuestars=request.POST.get('filtrostars',"")
        if valuetype != "" and valuestars != "":
            lista=Hotel.objects.filter(tipo=valuetype,stars=valuestars)
        elif valuestars == "" and valuetype != "":
            lista=Hotel.objects.filter(tipo=valuetype)
        elif valuetype == "" and valuestars != "":
            lista=Hotel.objects.filter(stars=valuestars)
        context = {'lista':lista,'user':request.user.username,'listausers':listauser,'condicion':""}

    if request.user.is_authenticated():
        us=PaginaUsuario.objects.get(user=request.user.username)
        context = {'lista':lista,'user':request.user.username,'condicion':"",'color':us.color,'size':us.size,'listausers':listauser}

    return render_to_response('alojamiento.html', context, context_instance = RequestContext(request))


def alojamientos_id(request,id):

    lista=Hotel.objects.get(id=id)
    listimages=Imagen.objects.filter(hid=lista.id)
    listauser=PaginaUsuario.objects.all()
    listcoms=""
    if request.method == 'POST':
        h_us = HotelesUsuario(hotel=lista,user=request.user.username)
    if request.method =='POST':
        value = request.POST.get('comentarios', "")
        if value !="":
            cot=Comentario(hid=lista.id,com=lista,text=value)
            cot.save()
        else:
            h_us.save()


    listcoms=Comentario .objects.filter(hid=lista.id)
    context = {'lista':listimages[0:5],'condicion':"",'url':lista.url,'name':lista.name,
                'address':lista.address,'comentarios':listcoms,'type':lista.tipo,'stars':lista.stars,
                'user':request.user.username,'listausers':listauser}
    if request.user.is_authenticated():
        us=PaginaUsuario.objects.get(user=request.user.username)
        context = {'lista':listimages[0:5],'condicion':"",'url':lista.url,'name':lista.name,
                    'address':lista.address,'comentarios':listcoms,'type':lista.tipo,'stars':lista.stars,
                    'color':us.color,'size':us.size,'user':request.user.username,'listausers':listauser}

    return render_to_response('alojamiento_id.html', context,context_instance = RequestContext(request))

def usuario(request,usuario):
    value=""
    siz=""
    title=""
    us=PaginaUsuario.objects.get(user=usuario)
    listhotels=HotelesUsuario.objects.filter(user=usuario)
    listauser=PaginaUsuario.objects.all()

    if request.method =='POST':
        value = request.POST.get('css', "")
        siz= request.POST.get('size', "")
        title= request.POST.get('title', "")
        us=PaginaUsuario.objects.get(user=usuario)
        if value != "" :
            us.color=value;
        if siz != "":
            us.size=siz;
        if title != "":
            us.title=title;
    us.save()

    value=us.color
    siz=us.size
    title=us.title
    print "value "+value
    context={'lista':listhotels,'color':value,'usuario':usuario,'size':siz,'title':title,
             'user':request.user.username,'listausers':listauser,'condicion':""}
    return render_to_response('usuario.html', context, context_instance = RequestContext(request))

def usuario_xml(request,usuario):
    us=PaginaUsuario.objects.get(user=usuario)
    listhotels=HotelesUsuario.objects.filter(user=usuario)
    listauser=PaginaUsuario.objects.all()
    f = open('templates/user_xml.xml', 'r')
    xml=f.read()
    return HttpResponse(xml, content_type='text/xml')

def about(request):
    lista=Hotel.objects.all()
    listauser=PaginaUsuario.objects.all()
    context={'listausers':listauser,'user':request.user.username}
    if request.user.is_authenticated():
        us=PaginaUsuario.objects.get(user=request.user.username)
        context={'listausers':listauser,'user':request.user.username,'color':us.color,'size':us.size}
    return render_to_response('about.html', context, context_instance = RequestContext(request))
