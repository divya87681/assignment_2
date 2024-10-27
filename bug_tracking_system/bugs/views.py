from django.shortcuts import render, redirect
from .models import Bug
from .forms import BugForm

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})

def bug_create(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(request, 'bugs/bug_form.html', {'form': form})
