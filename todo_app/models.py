from django.db import models
from django.utils import timezone

from django.db import models
from django.urls import reverse

#to set ToDoItem default due dates
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

#extends Django's django.db.models.Model superclass
class ToDoList(models.Model):
    #declare title field, w max length and required uniqueness
    title = models.CharField(max_length=100, unique=True)

    #returns URL for particular data item
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    #declare ToDo item description
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    #declared as foreign key, linnks ToDoItem back to ToDoList
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        #sets default ordering for ToDoItems
        ordering = ["due_date"]