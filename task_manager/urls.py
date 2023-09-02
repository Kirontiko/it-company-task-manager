from django.urls import path

from task_manager.views import (IndexView,
                                WorkerListView,
                                TaskListView,
                                TaskTypeListView,
                                PositionListView,
                                WorkerDetailView,
                                TaskDetailView,
                                WorkerCreateView,
                                TaskCreateView,
                                PositionCreateView,
                                TaskTypeCreateView, TaskTypeUpdateView, WorkerUpdateView, PositionUpdateView,
                                TaskUpdateView, WorkerDeleteView, TaskDeleteView, TaskTypeDeleteView,
                                PositionDeleteView, TaskUpdateWorkerView, PositionDetailView, TaskTypeDetailView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/",
         WorkerDetailView.as_view(),
         name="worker-detail"),
    path("workers/create/",
         WorkerCreateView.as_view(),
         name="worker-create"),
    path("workers/<int:pk>/update/",
         WorkerUpdateView.as_view(),
         name="worker-update"),
    path("workers/<int:pk>/delete/",
         WorkerDeleteView.as_view(),
         name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/",
         TaskDetailView.as_view(),
         name="task-detail"),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/update_worker/",
         TaskUpdateWorkerView.as_view(),
         name="task-update-worker"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task_types/create/",
         TaskTypeCreateView.as_view(),
         name="task_type-create"),
    path("task_types/<int:pk>/update/",
         TaskTypeUpdateView.as_view(),
         name="task_type-update"),
    path("task_types/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(),
         name="task_type-delete"),
    path("task_types/<int:pk>/",
         TaskTypeDetailView.as_view(),
         name="task_type-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/",
         PositionCreateView.as_view(),
         name="position-create"),
    path("positions/<int:pk>/update/",
         PositionUpdateView.as_view(),
         name="position-update"),
    path("positions/<int:pk>/delete/",
         PositionDeleteView.as_view(),
         name="position-delete"),
    path("positions/<int:pk>/",
         PositionDetailView.as_view(),
         name="position-detail")
]

app_name = "task_manager"
