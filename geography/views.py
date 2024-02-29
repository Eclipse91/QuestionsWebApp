from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from .models import Country
from random import randint, choice
import json


def index(request):
    '''
    Render the Home page with an introduction to the application and initiate the Geography game.
    '''
    # import pdb; pdb.set_trace()
    n_states = len(Country.objects.all())
    template = loader.get_template("geography/geography.html")
    country = randint(1,n_states)
    continents = [
                    {'name': 'Asia', 'checked': False},
                    {'name': 'Europe', 'checked': False},
                    {'name': 'Africa', 'checked': False},
                    {'name': 'North America', 'checked': False},
                    {'name': 'South America', 'checked': False},
                    {'name': 'Oceania', 'checked': False},
                ]
    country = Country.objects.filter(id=country)

    context = {
        'states': country,
        "total": 0,
        "questions": 0,
        'continents': continents
    }
    return HttpResponse(template.render(context, request))

def answer(request, country, total, questions, continents):
    '''
    Handle the user's answer submission, check correctness, and generate a new question.
    '''
    # import pdb; pdb.set_trace()
    my_choice = request.POST.get('myChoice')

    try:
        questions += 1
        if Country.objects.get(country=country).capital.upper() ==  my_choice.upper():
            total += 1
    except (KeyError, Country.DoesNotExist):
        return render(request, 'geography/geography.html')
    else:
        valid_json_string = continents.replace("'", "\"").replace("True", "true").replace("False", "false")
        continents = json.loads(valid_json_string)

        # Create the query to obtain a new country
        filtered_continents = [continent['name'] for continent in continents if continent['checked'] is not False]
        q_objects = Q()
        for continent in filtered_continents:
            q_objects |= Q(continent__icontains=continent)
        countries_not_in_continents = Country.objects.exclude(q_objects)
        ids = countries_not_in_continents.values_list('id', flat=True)
        new_country = choice(ids)
        country = Country.objects.filter(id=new_country)

        context = {
            'states': country,
            'total': total,
            'questions': questions,
            'continents': continents
        }
        template = loader.get_template('geography/geography.html')

        return HttpResponse(template.render(context, request))

def reset(request, country, continents):
    '''
    Reset the statistics.
    '''
    # import pdb; pdb.set_trace()
    valid_json_string = continents.replace("'", "\"").replace("True", "true").replace("False", "false")
    continents = json.loads(valid_json_string)

    total = 0
    questions = 0
    country = Country.objects.filter(country=country)

    context = {
        'states': country,
        'total': total,
        'questions': questions,
        'continents': continents
    }
    template = loader.get_template('geography/geography.html')

    return HttpResponse(template.render(context, request))

def filter(request, total, questions):
    '''
    Handle continent filtering, generate a new question, and keep the statistics.
    '''
    # import pdb; pdb.set_trace()
    continents = [
                request.POST.get('asia'), 
                request.POST.get('europe'), 
                request.POST.get('africa'), 
                request.POST.get('north america'), 
                request.POST.get('south america'), 
                request.POST.get('oceania'),
                ]
    continents_checkbox = [
                    {'name': 'Asia', 'checked': True if continents[0] != None else False},
                    {'name': 'Europe', 'checked': True if continents[1] != None else False},
                    {'name': 'Africa', 'checked': True if continents[2] != None else False},
                    {'name': 'North America', 'checked': True if continents[3] != None else False},
                    {'name': 'South America', 'checked': True if continents[4] != None else False},
                    {'name': 'Oceania', 'checked': True if continents[5] != None else False},
                    ]

    # Create the query to obtain a new country
    filtered_continents = [continent for continent in continents if continent is not None]
    q_objects = Q()
    for continent in filtered_continents:
        q_objects |= Q(continent__icontains=continent)
    countries_not_in_continents = Country.objects.exclude(q_objects)
    ids = countries_not_in_continents.values_list('id', flat=True)
    new_country = choice(ids)
    country = Country.objects.filter(id=new_country)

    context = {
        'states': country,
        'total': total,
        'questions': questions,
        'continents': continents_checkbox
    }
    template = loader.get_template('geography/geography.html')

    return HttpResponse(template.render(context, request))
