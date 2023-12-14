from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.urls import reverse

from .models import Task
from .forms import TaskForm


def taskView(request):
    list_tasks = Task.objects.all()
    form = TaskForm()
    return render(request, "index.html", context={"tasks": list_tasks,'form': form})


@csrf_exempt
@require_POST
def update_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    try:
        completed_str = request.POST.get("completed", "").lower()
        completed = completed_str == "true"

        task.completed = completed
        task.save()

        status = "completed" if completed else "not completed"
        return JsonResponse({"status": status})
    except ValueError:
        return JsonResponse({"error": "Invalid value for completed"}, status=400)


def create_task_modal(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app:create_task_modal'))
    form = TaskForm()
    return render(request, 'create_task_modal.html', {'form': form})