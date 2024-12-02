from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Todo ({self.title}, {self.user}, {self.done})"
    
    class Meta:
        ordering = [
            "done",
            "-updated_at",

        ]

        verbose_name = "Todo"
        verbose_name_plural = "Todos"
    

