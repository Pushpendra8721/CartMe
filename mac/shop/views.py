from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Order,OrderUpdate
from math import ceil
import json

def index(request):
    #products= product.objects.all()
    ##Slides= n//4 + ceil((n/4) + (n//4))

    allprods=[]
    catprods=product.objects.values('chategorie','id')
    cats={item['chategorie'] for item in catprods}
    for cat in cats:
        prods=product.objects.filter(chategorie=cat)
        n= len(prods)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allprods.append([prods,range(1,nSlides),nSlides])
    #params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    #allprods=[[products,range(1,nSlides),nSlides],
            # [products,range(1,nSlides),nSlides],
             #[products,range(1,nSlides),nSlides]]
    params={"allprods":allprods}
    return render(request,"shop/index.html", params)
def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        desc=request.POST.get("desc","")
        c=Contact(name=name,email=email,phone=phone,desc=desc)
        c.save()
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].item_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def searchMatch(query, item):
    if query in item.product_name or query in item.chategorie:
        return True
    else:
        return False

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = product.objects.values('chategorie', 'id')
    cats = {item['chategorie'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(chategorie=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<1:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def products(request,myid):
    products=product.objects.filter(id=myid)
    print(products)
    return render(request,'shop/products.html',{"products":products[0]})

def checkout(request):
    if request.method=="POST":
        item_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(item_json=item_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
