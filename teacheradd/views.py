from django.shortcuts import render,redirect
from api.models import Teacher
from .forms import PostForm
from django.contrib import messages
from django.views.generic import View

# Create your views here.

def check_user(request):
    if request.method == "POST":
        username = request.POST['u']
        request.session['username'] = username
        try:
            user=Teacher.objects.get(username=username)
            return redirect('teacheradd.views.fill_details')
        except Teacher.DoesNotExist:
            messages.error(request,'Invalid username')
            return redirect('teacheradd.views.check_user')
    return render(request,'check_user.html')


def fill_details(request):
    if request.method =="POST":
        form=PostForm(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.username=request.session.get('username')
            data.save()
            return render(request,'check_user.html')
    else:
        form=PostForm()
    return render(request,'fill_details.html',{'form':form})