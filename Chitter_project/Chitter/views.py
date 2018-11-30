from django.shortcuts import render

peeps = [
    {
        'author': 'Fred Bloggs',
        'title': 'First Peep',
        'content': 'This is the first peep',
        'date_posted': '30th November 2018'
    },
    {
        'author': 'Mary Poppins',
        'title': 'Second Peep',
        'content': 'This is the second peep',
        'date_posted': '30th November 2018'
    }

]

def home(request):
    context = {
        'peeps': peeps
    }
    return render(request, 'chitter/home.html', context)

def about(request):
    return render(request, 'chitter/about.html', {'title': 'About'})
