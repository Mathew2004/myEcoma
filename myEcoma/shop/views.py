from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json


# Create your views here.
def index(request):
    products = Product.objects.all()
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1,nSlides), nSlides])

    params = {'allProds': allProds, }
    return render(request, 'shop/index.html',params)

def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search',default="")
    products = Product.objects.all()
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        if n != 0:
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds, 'searchRes':query }
    if len(allProds)==0 or len(query)<3:
        params = {'msg':'Please make sure to enter relevant search query'}
    return render(request, 'shop/search.html', params)



def cart(request):
    products = Product.objects.all()
    
    return render(request, 'shop/cart.html', {'products':products})


def products(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))

    context = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    for i in range(1,nSlides):
        val = products[i].product_name
        print(val)
    #return HttpResponse(val)
    return render(request, 'shop/products.html',context)


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemJson", "")
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        add1 = request.POST.get("address1","")
        add2 = request.POST.get("address2","")
        phone = request.POST.get("phone","")
        zip = request.POST.get("zip","")


        order = Orders(items_jeson=items_json, name=name, email=email, phone=phone, address1=add1,address2=add2,zip=zip)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True;
        id = order.order_id;
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')






    params = {'search': search}
    return render(request, 'shop/search.html', params)


def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/productView.html", {'product': product[0]})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("txtName","")
        email = request.POST.get("txtEmail","")
        phone = request.POST.get("txtPhone","")
        msg = request.POST.get("txtMsg","")

        contact = Contact(name=name, email=email, phone=phone, msg=msg)
        contact.save()

    return render(request, 'shop/contact.html')



'''
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:

                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({'status':'success','updates':updates, 'itemsJson':order[0].items_jeson}, default=str)

                return HttpResponse(response)
            else:

                return HttpResponse("{'status':'noitem'}")
        except Exception as e:
            return HttpResponse("{'status':'error'}")

    return render(request, 'shop/tracker.html')
'''

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_jeson}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')
'''
def product(request):
    customerDataList = Product.objects.filter(
        vendor=request.user)
    temp = []
    for i in customerDataList:
        temp.append(i)

    context = {
        'customerData': temp,
    }
    return render(request, 'navbar.html', context)


'''