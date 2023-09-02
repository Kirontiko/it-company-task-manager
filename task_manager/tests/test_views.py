from datetime import date

from django import http
from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from task_manager.models import (Task,
                                 Position,
                                 TaskType,
                                 Worker)
from task_manager.views import TaskUpdateWorkerView

WORKERS_URL = reverse("task_manager:worker-list")
TASKS_URL = reverse("task_manager:task-list")
TASK_TYPES_URL = reverse("task_manager:task-type-list")
POSITIONS_URL = reverse("task_manager:position-list")


class PublicViewsTests(TestCase):
    def test_login_required_workers_view(self):
        response = self.client.get(WORKERS_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_tasks_view(self):
        response = self.client.get(TASKS_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_task_types_view(self):
        response = self.client.get(TASK_TYPES_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_positions_view(self):
        response = self.client.get(POSITIONS_URL)

        self.assertNotEqual(response.status_code, 200)

class PrivateViewsTests(TestCase):

    def setUp(self) -> None:
        self.workers_paginate_by = 10
        self.tasks_paginate_by = 6
        for index in range(11):
            Worker.objects.create_user(
                username=f"Test{index}",
                password=f"TestPassword12{index}",
                email="example@example.com",
                first_name=f"Robot{index}",
                last_name=f"Smith{index}",
                position=Position.objects.create(name=f"Developer{index}")
            )
        self.client.force_login(Worker.objects.get(id=1))

        for index in range(11):
            task = Task.objects.create(
                name=f"Task{index}",
                description="ASD",
                deadline=date.today(),
                is_completed=False,
                priority="UI",
                task_type=TaskType.objects.create(name=f"TaskType{index}"),

            )
            task.assignees.set(list(get_user_model().objects.all()))
            task.save()


    def test_retrieve_workers(self):
        response = self.client.get(WORKERS_URL)
        workers_first_page = Worker.objects.all()[:self.workers_paginate_by]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers_first_page)
        )

    def test_retrieve_tasks(self):
        response = self.client.get(TASKS_URL)
        tasks_first_page = Task.objects.all()[:self.tasks_paginate_by]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks_first_page)
        )

    def test_retrieve_task_types(self):
        response = self.client.get(TASK_TYPES_URL)
        task_types_first_page = TaskType.objects.all()[:self.tasks_paginate_by]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_types_first_page)
        )

    def test_retrieve_positions(self):
        response = self.client.get(POSITIONS_URL)
        positions_first_page = Position.objects.all()[:self.workers_paginate_by]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            list(response.context["position_list"]),
            list(positions_first_page)
        )

    def test_search_worker_by_username(self):
        searched_worker = "Test1"
        response = self.client.get(WORKERS_URL, {"username": searched_worker})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]),
            list(Worker.objects.filter(username__icontains=searched_worker))
        )

    def test_search_task_by_name(self):
        searched_task = "Task3"
        response = self.client.get(TASKS_URL, {"name": searched_task})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(Task.objects.filter(name__icontains=searched_task))
        )

    def test_search_task_by_name(self):
        searched_task_type = "TaskType5"
        response = self.client.get(TASK_TYPES_URL, {"name": searched_task_type})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(TaskType.objects.filter(name__icontains=searched_task_type))
        )

    def test_search_position_by_name(self):
        searched_position = "Developer4"
        response = self.client.get(POSITIONS_URL, {"name": searched_position})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(Position.objects.filter(name__icontains=searched_position))
        )

    def test_assign_worker_to_task(self):
        worker = Worker.objects.create_user(
            username=f"Kevin123",
            password=f"TestPassword12",
            email="example@example.com",
            first_name=f"Robot",
            last_name=f"Smith",
            position=Position.objects.create(name="Project Manager")
        )
        task = Task.objects.get(pk=1)
        url = reverse('task_manager:task-update-worker', kwargs={'pk': task.pk})
        factory = RequestFactory()
        request = factory.post(url)

        request.user = worker

        response = TaskUpdateWorkerView.as_view()(request, pk=task.pk)

        self.assertEqual(response.status_code, 302)

        self.assertIn(worker, task.assignees.all())

        response = TaskUpdateWorkerView.as_view()(request, pk=task.pk)

        self.assertEqual(response.status_code, 302)

        self.assertNotIn(worker, task.assignees.all())
