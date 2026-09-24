from django.shortcuts import render, redirect
from .forms import QuoteRequestForm


def home(request):
    from .models import Review

    reviews = Review.objects.all().order_by('-created_at')[:3]

    return render(request, 'core/home.html', {
        'reviews': reviews
    })


def services(request):
    return render(request, 'core/services.html')


def quote(request):

    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('quote_success')

    else:
        form = QuoteRequestForm()

    return render(request, 'core/quote.html', {
        'form': form
    })


def quote_success(request):
    return render(request, 'core/quote_success.html')
def samples(request):
    from .models import Sample

    all_samples = Sample.objects.all().order_by('-created_at')

    return render(request, 'core/samples.html', {
        'samples': all_samples
    })
def reviews(request):
    from .models import Review

    all_reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'core/reviews.html', {
        'reviews': all_reviews
    })
def contact(request):
    return render(request, 'core/contact.html')