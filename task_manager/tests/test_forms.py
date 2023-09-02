from django.contrib.auth import get_user_model
from django.test import TestCase
from datetime import datetime, date

from task_manager.forms import (Worker,
                                WorkerCreationForm,
                                WorkerPositionUpdateForm,
                                TaskCreationForm,
                                TaskUpdateForm)
from task_manager.models import Position, TaskType


class CreationOrUpdateWorkerFormTest(TestCase):
    def setUp(self) -> None:
        password = "TestPass123"

        self.form_data = {
            "username": "Kirontiko",
            "password1": password,
            "password2": password,
            "position": Position.objects.create(name="Developer"),
            "email": "example@example.com",
            "first_name": "Joh",
            "last_name": "Smih"
        }
        self.position = {
            "position": Position.objects.get(name="Developer")
        }


    def test_worker_creation_form(self):

        form = WorkerCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        for key in form.cleaned_data:
            self.assertEqual(
                form.cleaned_data[key], self.form_data[key]
            )


    def test_worker_update_form_with_position_valid(self):
        form = WorkerPositionUpdateForm(data=self.position)
        self.assertTrue(form.is_valid())

    def test_worker_update_form_with_position_invalid(self):
        self.form_data["position"] = "123"
        form = WorkerPositionUpdateForm(data=self.form_data)
        self.assertFalse(form.is_valid())


class CreateOrUpdateTaskForm(TestCase):
    def setUp(self) -> None:
        Position.objects.create(name="Developer")
        for worker in range(4):
            Worker.objects.create_user(
                username=f"Test{worker}",
                password="TestPass",
                email="TestExample@ex.com",
                position=Position.objects.get(name="Developer"),
                first_name="Test",
                last_name="test"
            )
        self.creation_form_data = {
            "name": "Task1",
            "description": "ASD",
            "deadline": date.today(),
            "is_completed": False,
            "priority": "UI",
            "task_type": TaskType.objects.create(name="TaskType1"),
            "assignees": list(get_user_model().objects.all())
        }

    def test_task_creation_form(self):
        form = TaskCreationForm(data=self.creation_form_data)
        self.assertTrue(form.is_valid())

        for key in form.cleaned_data:

            if key == "assignees":
                form.cleaned_data[key] = list(form.cleaned_data[key])
            self.assertEqual(
                form.cleaned_data[key], self.creation_form_data[key]
            )

    def test_task_creation_form_with_deadline_invalid(self):
        self.creation_form_data["deadline"] = datetime.strptime(
            "2022-01-01", "%Y-%m-%d"
        ).date()
        form = TaskCreationForm(
            data=self.creation_form_data
        )
        self.assertFalse(form.is_valid())

    def test_task_creation_form_with_deadline_valid(self):
        self.creation_form_data["deadline"] = datetime.strptime(
            "2024-01-01", "%Y-%m-%d"
        ).date()
        form = TaskCreationForm(
            data=self.creation_form_data
        )
        self.assertTrue(form.is_valid())

    def test_task_update_form(self):
        del self.creation_form_data["task_type"]
        form = TaskUpdateForm(data=self.creation_form_data)
        self.assertTrue(form.is_valid())

        for key in form.cleaned_data:

            if key == "assignees":
                form.cleaned_data[key] = list(form.cleaned_data[key])
            self.assertEqual(
                form.cleaned_data[key], self.creation_form_data[key]
            )

    def test_task_update_form_with_deadline_valid(self):
        del self.creation_form_data["task_type"]
        self.creation_form_data["deadline"] = datetime.strptime(
            "2024-01-01", "%Y-%m-%d"
        ).date()
        form = TaskUpdateForm(
            data=self.creation_form_data
        )
        self.assertTrue(form.is_valid())

    def test_task_update_form_with_deadline_invalid(self):
        del self.creation_form_data["task_type"]
        self.creation_form_data["deadline"] = datetime.strptime(
            "2022-01-01", "%Y-%m-%d"
        ).date()
        form = TaskUpdateForm(
            data=self.creation_form_data
        )
        self.assertFalse(form.is_valid())
