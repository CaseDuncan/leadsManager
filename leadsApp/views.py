from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from leadsApp.models import Lead


from leadsApp.serializers import LeadSerializer

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
    leads = Lead.objects.all()
    serializer = LeadSerializer(leads, many=True)
    return Response(serializer.data)


"""
view for get a single lead
"""


@api_view(['GET'])
def getLead(request, pk):
    lead = Lead.objects.get(id=pk)
    serializer = LeadSerializer(lead, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addLead(request):
    if request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)