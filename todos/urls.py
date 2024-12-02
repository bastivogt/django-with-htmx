from django.urls import path

from .views import index, new, edit, edit_done
urlpatterns = [
    
    path("", index, name="todos-index"),
    path("new/", new, name="todos-new"),
    path("edit/<int:id>/", edit, name="todos-edit"),
    path("edit-done/<int:id>/", edit_done, name="todos-edit-done")

]
