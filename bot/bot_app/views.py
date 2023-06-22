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
        
        if incoming_msg in ["hi", "hello", "hey"]:
            response= "*Hi, welcome to Jellybean Goodscenes bot* \n Are you from bangalore? Reply with Yes or No."
            msg.body(response)
        elif incoming_msg.startswith('yes'):
            response="Here is the list of experiences that you can choose from, type the name that you want to choose: \n 1.sushi making workshop \n 2.Wine tasting \n 3.Pottery workshop \n 4.Arcade"
            msg.body(response)
        elif incoming_msg.startswith('no'):
            response="Sorry, we are currently available only in Bangalore. \n"
            msg.body(response)
        elif 'sushi' in incoming_msg:
            response="Here are the details for Sushi making workshop: \n"
            msg.body(response)
        elif 'pottery' in incoming_msg:
            response="Here are the details for pottery workshop: \n"
            msg.body(response)
        elif 'wine' in incoming_msg:
            response="Here are the details for wine tasting workshop: \n"
            msg.body(response)
        elif 'arcade' in incoming_msg:
            response="Here are the details for Arcade: \n"
            msg.body(response)
        else:
            response="Sorry, we dont have that option available, Thankyou for using our bot."
            msg.body(response)
        
        return HttpResponse(str(resp))