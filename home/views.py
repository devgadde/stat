from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'home/welcome.html')

def me(request):

    return render(request,'home/myself.html')


def bootstrap(request):
    return render(request,'home/bootstrap.html')

def offers(request):
    return render(request,'home/offers.html')





