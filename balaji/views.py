from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'ganagdhara','age':21}
    return render(request, 'jinja_printing.html',context=d)