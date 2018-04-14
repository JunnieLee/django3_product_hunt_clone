from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


# Create your views here.
def home(request):
	products = Product.objects # Now this id gonna go and get all the Products objects	
	return render(request, 'products/home.html', {'products':products})


@login_required(login_url="/accounts/login")  # only the logged in can access this create page
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'): 
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.pub_date = timezone.datetime.now() # these are automatically generated
			product.hunter = request.user
			product.save()
			return redirect(to='detail', product_id=product.id)

		else:
			return render(request, 'products/create.html', {'error': 'All fields are required.'})	
				
	else:	
		return render(request, 'products/create.html')	



def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/detail.html', {'product':product})



@login_required(login_url="/accounts/login") # you can only vote when you're logged in
def upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect(to='detail', product_id=product.id)


@login_required # you can only vote when you're logged in
def upvote_at_home(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect(to='home')	