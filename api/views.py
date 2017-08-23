from django.shortcuts import render, render_to_response

def index(request):
   context = {'user': request.user}
   return render(request, 'api/index.html', context)
