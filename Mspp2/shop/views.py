from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from time import time
from math import ceil
from .models import *
import json,ast,razorpay
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

razorpay_client=razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))

def aindex(request):#it adds products
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("/success")
    else:
        form = ImageForm()

    return render(request, 'addpors.html', {'form': form})

def checkout(request):#for cart products payment
    if request.method == "POST":
        b1 = request.POST.get('joj', 'off')
        b2 = request.POST.get('jo', 'off')
        email = request.POST.get('emale')
        name = request.POST.get("naam")
        address = request.POST.get('pata')
        city = request.POST.get('shehar')
        state = request.POST.get('state')
        zip0 = request.POST.get('zip')
        items=request.POST.get('items')
        order_id=request.POST.get('iorder')
        order = Orders(user=request.user,approved=False,order_id=order_id,name=name , email=email,items=items,
                       address=address, city=city, state=state, zip_code=zip0)
        if b2=="on":
            order.approved=True
            order.save()
            return redirect("/orders")
        elif b1=="on":
            order.save()
            odr=Orders.objects.all()[0].items
            print(odr)
            currency="INR"
            amount=int(odr)*100
            razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
            razorpay_order_id=razorpay_order['id']
            callback_url = 'paymenthandler/'
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
 
            return render(request, 'jojo.html', context=context)
        
        
    return render(request,'chko.html')
def showproducts(request):#showing products on products page
    if request.method == "GET":
        images = Image.objects.all()
        n = len(images)
        return render(request, "product.html", {'shop_image': images, 'range': range(1, n)})
        
def orders(request):#orders and tracking system
    itemz=Orders.objects.filter(user=request.user)
    s=[]    
    for i in range(len(itemz)):
        try:
            k=json.loads(itemz[i].items)
            p=itemz[i].Tracker
            for x in k.values():
                m=[]
                m.append(x['name'])
                m.append(p)
                m.append(x['price']*x['q'])
                s.append(m)
        except:
            m=itemz[i].items.strip('][').replace('\'','').split(",")
            k=itemz[i].Tracker
            m.append(k)
            s.append(m)
    return render(request,"orders.html",{'price':s})



def check(request, myid):#an individual product page
    imag = Image.objects.filter(id=myid)

    return render(request, "check.html", {'image': imag[0]})
def done(request):
    if request.method=="POST":
        return HttpResponse("jm")
    return render(request,'proof.html')

def search(request):
    search=request.GET['search']
    if len(search)>73:
        searchitems=[]
    else:
        searchitems1=Image.objects.filter(name__icontains=search)
        searchitems2=Image.objects.filter(desc__icontains=search)
        searchitems=searchitems1.union(searchitems2)

    if len(searchitems) == 0:
        messages.warning(request,"No search results found")
    return render(request,"search.html",{"searchitems":searchitems,'query':search})


def payment(request):
    currency="INR"
    amount=20000
    

    razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order_id=razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'jojo.html', context=context)

@csrf_exempt
def paymentHandler(request):
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return HttpResponse("ok")
                except:
 
                    # if there is an error while capturing payment.
                    return HttpResponse("not ok")
            else:
 
                # if signature verification fails.
                return HttpResponse("not ok")
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

def pay(request, paid):
    imag = Image.objects.filter(id=paid)
    
    if request.method == "POST":
        b1 = request.POST.get('joj', 'off')
        b2 = request.POST.get('jo', 'off')
        email = request.POST.get('emale')
        name = request.POST.get("naam")
        address = request.POST.get('pata')
        city = request.POST.get('shehar')
        state = request.POST.get('state')
        zip0 = request.POST.get('zip')
        items =[(imag[0].name),int(imag[0].price)]

        order = Orders(user=request.user,approved=False, name=name, items=items, email=email,
                       address=address, city=city, state=state, zip_code=zip0)

        if b1 == 'on':
           
            order.save()
            odr=Orders.objects.all()[0].items.split(',')[1].replace(']','')
            currency="INR"
            amount=int(odr)*100
            razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
            razorpay_order_id=razorpay_order['id']
            callback_url = 'paymenthandler/'
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url

            return render(request, 'jojo.html', context=context)
        

        if b2 == "on":
            order.approved = True
            order.save()
            return redirect("/orders")

    return render(request, "chko.html", {'image': imag[0]})

