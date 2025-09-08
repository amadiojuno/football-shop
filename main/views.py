from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406496416',
        'name': 'Amadio Juno Trisanto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)