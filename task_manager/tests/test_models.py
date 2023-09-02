from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import (
    Worker,
    Position,
    TaskType,
    Task
)


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="Test",
            password="TestPassword123",
            email="email@example.com",
            first_name="John",
            last_name="Smith",
            position=Position.objects.get(name="Developer")
        )
        self.task_type = TaskType.objects.create(
            name="Test1",
        )
        self.task = Task.objects.create(
            name=f"Task",
            description="ASD",
            deadline=date.today(),
            is_completed=False,
            priority="UI",
            task_type=TaskType.objects.get(name="Test1"),
        )
        self.task.assignees.set(list(get_user_model().objects.all()))
        self.task.save()

    def test_worker_str_repr(self):

        self.assertEqual(
            str(self.worker),
            f"{self.worker.username} "
            f"({self.worker.first_name} {self.worker.last_name})")

    def test_task_str_repr(self):

        self.assertEqual(
            str(self.task),
            f"{self.task.name} (deadline:{self.task.deadline})"
        )

    def test_task_type_str_repr(self):
        self.assertEqual(
            str(self.task_type),
            self.task_type.name
        )

    def test_position_str_repr(self):
        self.assertEqual(
            str(self.position),
            self.position.name
        )