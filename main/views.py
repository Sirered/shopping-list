from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Galih Ibrahim Kurniawan',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
