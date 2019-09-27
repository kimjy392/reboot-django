from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
from decouple import config
import requests
# Create your views here.

def create(request):
    return render(request, 'jobs/create.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        job = Job.objects.filter(name=name).first()
        if not job:
            fake = Faker('ko_KR')
            job = Job()
            job.name = name
            job.job = fake.job()
            job.save()
        api_key = config('GIPHY_API_KEY')
        url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job.job}&lang=ko'
        response = requests.get(url).json()
        try:
            image_url = response['data'][0].get('images').get('original').get('url')
        except:
            image_url = None
        context = {
            'job' : job,
            'image_url' : image_url
        }
        return render(request, 'jobs/result.html', context)
    else:
        redirect('jobs:create')