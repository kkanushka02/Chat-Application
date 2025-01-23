from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Account successfully created! Now, please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error creating your account. Please try again.")
    else:
        form = UserCreationForm()

    return render(request, 'chat/signup.html', {'form': form})

def home(request):
    return redirect('signup')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect('chatroom')  
        else:
            messages.error(request, "Invalid username or password.")  
    return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out.") 
    return redirect('login')  

@login_required
def chatroom(request):
    users = User.objects.exclude(id=request.user.id)  
    return render(request, 'chat/chatroom.html', {'users': users})

@login_required
def messages_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

   
    messages_list = Message.objects.filter(sender=request.user, receiver=user) | \
                    Message.objects.filter(sender=user, receiver=request.user)
    messages_list = messages_list.order_by('timestamp')

    # Handle message sending via POST (AJAX request)
    if request.method == "POST":
        message_text = request.POST.get('message')
        if message_text:
            new_message = Message.objects.create(
                sender=request.user,
                receiver=user,
                text=message_text
            )
            return JsonResponse({
                'sender': request.user.username,
                'text': new_message.text,
                'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            })

    return render(request, 'chat/messages.html', {
        'messages': messages_list,
        'user': user,
    })
