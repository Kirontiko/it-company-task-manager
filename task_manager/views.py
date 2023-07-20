from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from task_manager.forms import WorkerCreationForm, TaskCreationForm, WorkerPositionUpdateForm, TaskUpdateForm
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


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerPositionUpdateForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_manager/task_type_list.html"
    paginate_by = 10


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-type-list")



class PositionListView(generic.ListView):
    model = Position
    paginate_by = 10


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")
