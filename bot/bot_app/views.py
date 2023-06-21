from django.shortcuts import render
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()
        if incoming_msg=="hi":
            response= "*Hi, welcome to Jellybean Goodscenes bot*"
            msg.body(response)
        
        return HttpResponse(str(resp))