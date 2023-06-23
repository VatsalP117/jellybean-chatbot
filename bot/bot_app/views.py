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
            response="Here is the list of experiences that you can choose from, type the name that you want to choose: \n 1.Sushi Making Workshop \n 2.Wine Tasting \n 3.Baking \n 4.Arcade"
            msg.body(response)
        elif incoming_msg.startswith('no'):
            response="Sorry, we are currently available only in Bangalore. \n"
            msg.body(response)
        elif 'sushi' in incoming_msg  or incoming_msg=="1":
            response="""Learn to roll a variety of sushi with professional sushi chef and master-instructor, Amit Patra. During the fun and interactive workshop, you will be taken through his easy-to-follow rolling techniques before making your own rolls and learning how to adapt them with an array of fillings and toppings. Sushi Rolling Masterclass is for all sushi lovers and food enthusiasts!\n 
            What's Included: \n 1 welcome drink \n 1 appetizer \n All materials for sushi making (salmon, sticky rice, mayo etc.)
\n 1 dessert"""
            msg.body(response)
        elif 'pottery' in incoming_msg:
            response="Here are the details for pottery workshop: \n"
            msg.body(response)
        elif 'baking' in incoming_msg or incoming_msg=="3":
            response="Learn how to bake many popular items such as Travel Tea Time Cakes, Cream Icing And Pastries, Breads and many popular European Desserts in a fun packed 4 hours masterclass!"
            msg.body(response)
        elif 'wine' in incoming_msg or incoming_msg=="2":
            response=""" The Big Banyan Vineyards is a short drive away from the urban chaos, located on the outskirts of the city, near the iconic Big Banyan tree.At the vineyards, you can choose from 2 different types of tours: \n 
            Basic Tour: includes a tour and a detailed explanation of the wine making process. No tasting of wine. \n
            Wine Tasting Package: includes a tour and detailed explanation of the winemaking process and the winery and a guided walk through the vineyards. It is followed by one tasting. The wines you will  taste are: \n
            Langoor white wine \n
            Langoor red wine \n
            1 Big Banyan white wine \n
            Big Banyan Rosa rossa \n
            1 Big Banyan red wine \n
            Bellissima - dessert wine"""
            msg.body(response)
        elif 'arcade' in incoming_msg:
            response="Here are the details for Arcade: \n"
            msg.body(response)
        else:
            response="Sorry, we dont have that option available, Thankyou for using our bot."
            msg.body(response)
        
        return HttpResponse(str(resp))