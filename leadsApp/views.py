from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from leadsApp.models import Lead
from .leads import leads

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/leads/',
        'api/leads/<id>/',

        'api/leads/add/',

        'api/leads/<update>/<id>/',
        'api/leads/<delete>/<id>/',
    ]
    return Response(routes)


"""
view for get a list of all leads
"""


@api_view(['GET'])
def getLeads(request):
    # leads = Lead.objects.all()
    return Response(leads)


"""
view for get a single lead
"""


@api_view(['GET'])
def getLead(request, pk):
    lead = None
    for i in leads:
        if i['id'] == pk:
            lead = i
            break
    return Response(lead)
