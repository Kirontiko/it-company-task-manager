from django.shortcuts import render
from django.views import generic

from task_manager.models import (
    Worker,
    Position,
    TaskType,
    Task
)


class IndexView(generic.View):

    def get(self, request):
        context = {
            "num_workers": Worker.objects.count(),
            "num_tasks": Task.objects.count(),
            "num_positions": Position.objects.count(),
            "num_task_types": TaskType.objects.count()
        }

        return render(request,
                      "task_manager/index.html",
                      context=context)


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(generic.DetailView):
    model = Worker



class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task



class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_manager/task_type_list.html"
    paginate_by = 10


class PositionListView(generic.ListView):
    model = Position
    paginate_by = 10
