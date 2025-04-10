from django.shortcuts import render, redirect
from .models import Item1, Item2
from .cp_scraper import get_cp_data
from .hack_scraper import get_hack_data

# Create your views here.
def display_data(request):
    data1 = Item1.objects.all()
    data2 = Item2.objects.all()
    return render(request, 'webscraper/display.html', {
        'data1': data1,
        'data2': data2
    })

def run_scraper(request):
    Item1.objects.all().delete()
    Item2.objects.all().delete()

    df1 = get_hack_data()
    df2 = get_cp_data()

    for _, row in df1.iterrows():
        Item1.objects.create(
            name = row['Name'],
            date_time = row['Date & Time']
            )
    
    for _, row in df2.iterrows():
        Item2.objects.create(
            name = row['Name'],
            date_time = row['Date & Time']
        )

    return redirect('display_data')
