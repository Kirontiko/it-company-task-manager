from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from task_manager.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["position"]


class BaseTaskDeadlineValidationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["deadline"]

    def clean_deadline(self) -> str:
        deadline = self.cleaned_data["deadline"]
        if date.today() > deadline:
            raise ValidationError("Deadline is already expired! "
                                  f"You cannot set date earlier than {date.today()}")
        return deadline


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        assignees = forms.ModelMultipleChoiceField(
            queryset=get_user_model().objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date"
                }
            ),

        }


class TaskCreationForm(TaskForm, BaseTaskDeadlineValidationForm):
    class Meta:
        model = Task
        fields = TaskForm.Meta.fields
        widgets = TaskForm.Meta.widgets


class TaskUpdateForm(TaskForm, BaseTaskDeadlineValidationForm):
    class Meta:
        model = Task
        fields = ["name",
                  "description",
                  "deadline",
                  "is_completed",
                  "priority"]
        widgets = TaskForm.Meta.widgets
