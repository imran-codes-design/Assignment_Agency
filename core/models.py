from django.db import models


class QuoteRequest(models.Model):

    SERVICE_CHOICES = [
        ('Assignment', 'Assignment'),
        ('Essay', 'Essay'),
        ('Research Project', 'Research Project'),
        ('Dissertation', 'Dissertation'),
        ('IT Project', 'IT Project'),
        ('Presentation', 'Presentation'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    whatsapp = models.CharField(max_length=30)

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    project_title = models.CharField(max_length=200)

    requirements = models.TextField()

    deadline = models.DateField()

    word_count = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.project_title}"
class Sample(models.Model):

    CATEGORY_CHOICES = [
        ('Assignment', 'Assignment'),
        ('Essay', 'Essay'),
        ('Research Project', 'Research Project'),
        ('Dissertation', 'Dissertation'),
        ('IT Project', 'IT Project'),
        ('Presentation', 'Presentation'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    file = models.FileField(
        upload_to='samples/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
class Review(models.Model):

    name = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    review = models.TextField()

    rating = models.PositiveIntegerField(
        default=5
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.country}"