from django.shortcuts import render, redirect
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Project, Task
from .forms import ProjectForm, TaskForm


def home(request):
    data = {}
    data['projects'] = Project.objects.all()
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    return render(request, 'projects/home.html', data)


def update(request, pk):
    data = {}
    data['projects'] = Project.objects.all()
    project = Project.objects.get(pk=pk)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    return render(request, 'projects/home.html', data)


def delete(request, pk):
    data = {}
    data['projects'] = Project.objects.all()
    project = Project.objects.get(pk=pk)
    project.delete()
    form = ProjectForm()
    data['form'] = form
    return redirect('url_home')


def tasks(request, id_project):
    data = {}
    data['project'] = Project.objects.get(id=id_project)
    query = 'SELECT id, title, description, (gravity * urgency * trend) as priority ' \
            'FROM projects_task WHERE project_id = %s ORDER BY priority DESC' % id_project
    data['tasks'] = Task.objects.raw(query)
    # data['tasks'] = data['project'].task_set.all() # Exibe todas as tasks do projeto

    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.instance
        task.project = data['project']
        task.save()
        return redirect('url_tasks', id_project)

    data['form'] = form
    return render(request, 'projects/project.html', data)


def tasksupdate(request, id_project, id_task):
    data = {}
    data['project'] = Project.objects.get(id=id_project)
    query = 'SELECT id, title, description, (gravity * urgency * trend) as priority ' \
            'FROM projects_task WHERE project_id = %s ORDER BY priority DESC' % id_project
    data['tasks'] = Task.objects.raw(query)
    data['current_task'] = data['project'].task_set.get(pk=id_task)

    print("Update task: " + data['current_task'].title)

    form = TaskForm(request.POST or None, instance=data['current_task'])

    if form.is_valid():
        task = form.instance
        task.project = data['project']
        task.save()
        return redirect('url_tasks', id_project)

    data['form'] = form
    return render(request, 'projects/project.html', data)


def taskdelete(request, id_project, id_task):
    data = {}
    data['project'] = Project.objects.get(id=id_project)

    data['project'].task_set.get(pk=id_task).delete()
    print("Del task")

    form = ProjectForm()
    data['form'] = form
    return redirect('url_tasks', id_project)


def generate_report(request, id_project):
    data = {}
    data['project'] = Project.objects.get(id=id_project)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
