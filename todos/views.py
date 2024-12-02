from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

from .forms import TodoForm
from .models import Todo

# Create your views here.

@login_required(login_url="sevo-auth-sign-in")
def index(request):
    todos = Todo.objects.all().filter(user=request.user)
    return render(request, "todos/index.html", {
        "title": _("All Todos"),
        "todos": todos
    })


@login_required(login_url="sevo-auth-sign-in")
def new(request):
    todo = Todo(user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos-index")
    else:
        form = TodoForm(instance=todo)

    return render(request, "todos/new.html", {
        "title": _("New Todo"),
        "form": form
    })

@login_required(login_url="sevo-auth-sign-in")
def edit(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos-index")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/edit.html", {
        "title": todo.title,
        "form": form
    })


@login_required(login_url="sevo-auth-sign-in")
def edit_done(request, id):
    print("edit_done")
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id, user=request.user)
        todo.done = not todo.done
        print(todo)
        todo.save()
        #return redirect("todos-index")

        todos_all = Todo.objects.all().filter(user=request.user)
        return render(request, "todos/partials/_table.html", {
            "todos": todos_all
        })