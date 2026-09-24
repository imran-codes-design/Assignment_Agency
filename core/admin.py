from django.contrib import admin
from .models import QuoteRequest, Sample, Review


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'service',
        'project_title',
        'budget',
        'deadline',
        'created_at',
    )

    list_filter = (
        'service',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'project_title',
    )
from .models import QuoteRequest, Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'created_at',
    )

    list_filter = (
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'country',
        'rating',
        'created_at',
    )

    list_filter = (
        'country',
        'rating',
        'created_at',
    )

    search_fields = (
        'name',
        'country',
        'review',
    )