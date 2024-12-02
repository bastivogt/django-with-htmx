from django.urls import path

from .views import index, new, edit, edit_done, delete_index, delete
urlpatterns = [
    
    path("", index, name="todos-index"),
    path("new/", new, name="todos-new"),
    path("edit/<int:id>/", edit, name="todos-edit"),
    path("edit-done/<int:id>/", edit_done, name="todos-edit-done"),
    path("delete-index/<int:id>/", delete_index, name="todos-delete-index"),
    path("delete/<int:id>/", delete, name="todos-delete")

]
