from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messege = request.POST.get('messege')
        c = Contact(name=name, email=email, subject=subject, messege=messege)
        c.save()

        return render(request, 'mysite/index.html')
    else:
        return render(request, 'mysite/contact.html')