from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('estudantes/', views.listar_estudantes, name='listar_estudantes'),
    path('estudantes/adicionar/', views.adicionar_estudante, name='adicionar_estudante'),
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('disciplinas/adicionar/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('professores/', views.listar_professores, name='listar_professores'),
    path('professores/adicionar/', views.adicionar_professor, name='adicionar_professor'),
]
