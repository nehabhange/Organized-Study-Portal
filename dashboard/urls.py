from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete_note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes_detail"),

    path('homework',views.homework,name="homework"),
    path('update_hw/<int:pk>',views.update_hw,name="update_hw"),
    path('delete_hw/<int:pk>',views.delete_hw,name="delete_hw"),

    
    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update_todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete_todo"),

    path('books',views.books,name="books"),

    
]
