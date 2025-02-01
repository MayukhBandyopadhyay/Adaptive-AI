from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.title

class UserProfile(models.Model):  # ✅ Ensure this exists!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goals = models.TextField()
    skill_level = models.CharField(
        max_length=50,
        choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]
    )

    def __str__(self):
        return f"{self.user.username} Profile"

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(help_text="Progress in percentage")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.progress}%)"
