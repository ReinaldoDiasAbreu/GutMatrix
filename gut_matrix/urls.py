"""gut_matrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projects.views import home, update, delete, tasks, tasksupdate, taskdelete, generate_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('project_update/<int:pk>', update, name='url_update'),
    path('project_delete/<int:pk>', delete, name='url_delete'),
    path('tasks/<int:id_project>', tasks, name='url_tasks'),
    path('tasks_update/<int:id_project>/<int:id_task>', tasksupdate, name='url_tasks_update'),
    path('tasks_delete/<int:id_project>/<int:id_task>', taskdelete, name='url_tasks_delete'),
    path('report/<int:id_project>', generate_report, name='generate_report')
]

