from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from models import info
from models import orders
from django import forms
from datetime import date
from django.shortcuts import redirect
# Create your views here.

class registerform(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'

class registerformorders(forms.ModelForm):
    class Meta:
        model = orders
        fields = '__all__'


def id_generator(size=20, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def rand_to_cookie(rand):
    #cookie = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefgh'
    cookie = id_generator() + id_generator() + id_generator()
    cookie = rand[0] + cookie[1:]
    i=1
    while i < 20:
        cookie = cookie[0:i*3] + rand[i] + cookie[i*3+1:]
        i+=1
    return cookie

def cookie_to_rand(cookie):
    rand='12345678912345678900'
    rand = cookie[0] + rand[1:]
    i=1
    while i < 20:
        rand = rand[:i] + cookie[i*3] + rand[i+1:]
        i+=1
    return rand

def submit(request):
    mobnum = request.POST['mobnum']
    if info.objects.filter(ph_no=mobnum).exists():
        return HttpResponse('mobile number to be unique')
    else:
        passwd = request.POST['passwd']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        if gender == 'M':
            gender = True
        else:
            gender = False
        rand = id_generator()
        data = {'fname' : fname.title(), 'lname' : lname.title(),  'ph_no' : mobnum, 'email' : email, 'passwd' : passwd, 'address' : 'Please enter address of delivery', 'verify' : False, 'GenderIsMale' : gender, 'rand' : rand, 'TotalOrders' : 0}
        k = registerform()
        k = registerform(data)
        k.save()
        cookie_data = rand_to_cookie(rand)
        a=info.objects.get(ph_no=mobnum)
        response = render(request,'order.html', {'name':str(a.fname), 'address':str(a.address)})
        response.set_cookie(key='id', value=cookie_data)
        return response

def register(request):
    return render(request,'firstform.html')
def login(request):
    cookie_value = request.COOKIES.get('id')
    if cookie_value!= None :
        randkey = cookie_to_rand(cookie_value)
        if info.objects.filter(rand=randkey).exists():
            a=info.objects.get(rand=randkey)
            return HttpResponse("hey " + a.fname)
        else:
            cookie_value = rand_to_cookie(id_generator())
            return redirect("http://127.0.0.1:8000")
    else:
        return redirect("http://127.0.0.1:8000")
        
def placeorder(request):
    cookie_value = request.COOKIES.get('id')
    randkey = cookie_to_rand(cookie_value)
    if info.objects.filter(rand=randkey).exists():
        a=info.objects.get(rand=randkey)
        ordervalues = []
        ordervalues.append(request.POST.get('type1'))
        ordervalues.append(request.POST.get('type2'))
        ordervalues.append(request.POST.get('type3'))
        ordervalues.append(request.POST.get('type4'))
        ordervalues.append(request.POST.get('type5'))
        orders=[]
        orders.append(request.POST.get('one'))
        orders.append(request.POST.get('two'))
        orders.append(request.POST.get('three'))
        orders.append(request.POST.get('four'))
        orders.append(request.POST.get('five'))
        address = request.POST.get('address')
        quantity=' '
        count = 0
        for i in ordervalues:
            if orders[count]:
                quantity = quantity+i+'x'+orders[count]+' + '
                count = count + 1
        quantity = quantity[0:(len(quantity) - 3)]
        a.TotalOrders += 1
        a.save()
        orderid = a.fname+str(a.TotalOrders)
        dateplaced = date.today()
        data = {'orderid':orderid, 'custph':a.ph_no, 'metersquantity':quantity, 'status':'1', 'DatePlaced':dateplaced}
        k = registerformorders(data)
        k.save()
        return HttpResponse('thank you'+a.fname+' for placing order '+quantity)
    else:
        return HttpResponse('wrong')
