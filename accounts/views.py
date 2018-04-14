from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
	if request.method == 'POST':
		# User has info and wants an account now!
		if request.POST['password1'] == request.POST['password2']: # 비밀번호가 일치한다면
			try:
				user = User.objects.get(username=request.POST['username']) # 기존에 있던 username과 겹친다면 (1)
				return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
																		   	# 에러를 띄워라
			# (1)의 조건을 충족하지 않을 시 reuturn문을 뛰어넘고 바로 이 except문으로 옴															   
			except User.DoesNotExist: # 기존 username과 겹치는게 없다면 (+passwords match)
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				# 그 username과 password로 계정을 하나 새로 만들어라!
				auth.login(request, user) # 만든 계정으로 로그인을 시켜라! 	
				return redirect('home')	# 로그인 시킨 다음엔 그 로그인 된 상태 그대로 home 페이지로 데려가라...	
		else: # 비밀번호가 일치하지 않는다면		
			return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})		
	else:
		# User wants to enter info	
		return render(request, 'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		# auth.authenticate을 사용해서 해당 유저 정보가 유효한지 아닌지 확인할 단서를 제공할 수 있음!
		if user is not None: # 해당 user 정보가 유효하다면
			auth.login(request, user) # 로그인 시켜라!
			return redirect('home')	# 로그인 시킨 상태로 home페이지로 redirect시켜라!		
		else: # 해당 user정보가 유효하지 않다면 -> 에러를 띄워라 	
			return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})
	else: 
		return render(request, 'accounts/login.html')		

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')		