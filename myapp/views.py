
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,HttpResponse ,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth import authenticate ,login ,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
# Create your views here.
def base(request):
    return render(request,'main/base.html')
@login_required(login_url="/login/")
def index(request):
    allpro = Product.objects.filter(statu='Public')
    context = {
        'allpro':allpro
    }
    return render(request,'main/index.html',context)
def profile_view(request):
   
    categories = Categories.objects.all()
    price = Filter_price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    catid = request.GET.get('categories')
    price_id = request.GET.get('price_filter')
    color_id = request.GET.get('color_filter')
    brand_id = request.GET.get('brand_filter')
    Atoz_id = request.GET.get('AtoZ')
    ztoa_id = request.GET.get('ZtoA')
    Low_Price_id = request.GET.get('Low_Price')
    high_to_low_id = request.GET.get('high to low')
    Sort_By_new_id =request.GET.get('Sort_By_new')
    Sort_By_old_id =request.GET.get('Sort_By_Old')


    if catid:
        allpro = Product.objects.filter(category=catid)
    elif price_id:
        allpro = Product.objects.filter(filter_price=price_id)
    elif color_id:
        allpro = Product.objects.filter(color=color_id)
    elif  brand_id:
        allpro = Product.objects.filter( brand= brand_id)
    elif Atoz_id:
        allpro = Product.objects.filter(statu='Public').order_by('name')
    elif Low_Price_id:
        allpro = Product.objects.filter(statu='Public').order_by('price')
    elif ztoa_id:
        allpro = Product.objects.filter(statu='Public').order_by('-name')
    elif high_to_low_id:
        allpro = Product.objects.filter(statu='Public').order_by('-price')
    elif  Sort_By_new_id:
        allpro = Product.objects.filter( condition='New').order_by('-id')
    elif  Sort_By_old_id:
        allpro = Product.objects.filter( condition='Old').order_by('-id')
       

    else:
        allpro = Product.objects.filter(statu='Public')

    context = {
        'allpro':allpro,
        'categories':categories,
        'price':price ,
        'color':color,
        'brand':brand,
    }
    return render(request,'main/product.html',context)

def search_view(request):
    query = request.GET['query']
    allpro=Product.objects.filter(name__icontains=query)
    # allpro = Product.objects.filter(statu='Public')
    context={
           
            "allpro":allpro
        }
    return render(request,'main/search.html',context)
def product_single_view(request,id):
    allproduct= Product.objects.filter(id =id).first()
    context={
           
            "allproduct":allproduct
        }
    return render(request,'main/product_single.html',context)
def contect_view(request):
    if request.method =="POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contect = contect_us(
            name=name,
            email=email,
            subject=subject,
            message=message

        )
       
        subject = subject
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail( subject, message, email_from,['pk949542@gmail.com'] )
            contect.save()
            return redirect('index_page')
        except:
            return redirect('contect_page')

    return render(request,'main/contect.html')
def authentication_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        user = User.objects.create_user(username,email,pass1)
        user.first_name = first_name
        user.last_name =last_name
        user.save()
        return redirect('/authentication_page/')

    return render(request,'registration/auth.html')
def login_view(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username,password =password)
        if user is not None:
            login (request,user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request,'registration/auth.html')


def logout_view(request):
    logout(request)
    return redirect("login")

### cart



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index_page")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def checkout_view(request):
    amount_str = request.POST.get('amount')
    amount_float = float(amount_str)
    amount_int = int(amount_float)
    print( amount_int,"ppppppppppppppppppppk")
    payment=client.order.create({
       "amount": amount_int , # Rs. 200
        'currency' :'INR',
        'payment_capture':'1',
        })
    print(payment)
    order_id=payment['id']
    print(order_id)
 
    # Create a Razorpay Order
    
    return render(request,'cart/checkout.html')
def order_view(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        cart =request.session.get('cart')
        paid=request.session.get(' paid')
        
        print(paid,"pratap pad kro")
        order_id = request.POST.get('order_id')
        print(order_id)
        con ={
            'order_id':order_id
        }
        order = Order(
            user = user,
            first_name =first_name,
            last_name =last_name,
            country =country,
            state = state,
            city = city,
            address = address,
            pincode =pincode,
            phone=phone,
            email = email,
            amount =amount,
            payment_id= order_id,
            
       
        )

        order.save()
        for i in cart:
            a=(int(cart[i]['quantity']))
            b=(int(cart [i]['price']))
            total = a*b
            print(total)
            
            item_id =OrderItem(
                user=user,
                order =order,
                image= cart[i]['image'],
                product=cart[i]['name'],
                price=cart [i]['price'],
                quantity=cart[i]['quantity'],
                
                total=total

            )
            item_id.save()
        
           
        print(first_name,last_name,email,address,city,user,country,state,pincode,phone,order_id,amount)

        
    return render(request,'cart/order.html',con)
@csrf_exempt
def thankyou_view(request):
    if request.method == "POST":
        a = request.POST
        order_id =''
        for key ,val in a.items():
            if key =='rozarpay_order_id':
                order_id = val
                break
        user =Order.objects.filter(payment_id=order_id).first()
        user.paid =True
        print(user.paid,"user paid padddd")
        user.save
    return render(request,'cart/thankyou.html')
def yourorder_view(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order =OrderItem.objects.filter(user=user)
    con ={
       'order':order 
    }
    return render(request,'cart/yourorder.html',con)