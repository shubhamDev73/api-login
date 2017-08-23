from django.shortcuts import redirect

def fakeIndex(request):
    return redirect('/api/')
