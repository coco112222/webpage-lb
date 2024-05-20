from django.shortcuts import render

# Create your views here.
def go(r):
    
    return render(r,'index.html')

def about(r):
    return render(r,'about.html')

def menu(r):
    return render(r,'menu.html')

def offer(r):
    return render(r,'offer.html')

def login(r):
    h=r.POST.get('user')
    p=r.POST.get('pas')
    dick={'username':h,'password':p}
    return render(r,'log.html',dick)