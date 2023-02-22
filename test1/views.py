from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import json
import openai
# import os

# Create your views here.
def show_chat(response):
    """Show the main chat"""
    return render(response, "test1/chat.html", {})

def operate_msg(request):
    """Send a request to OpenAI with a custom message"""

    msg =  request.GET.get('msg')
    
    # openai.api_key = settings.OPENAI_KEY
    # if settings.OPENAI_KEY != "":
    #     response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=msg,
    #     temperature=0.3,
    #     max_tokens=60,
    #     # top_p=1.0,
    #     # frequency_penalty=0.0,
    #     # presence_penalty=0.0,
    #     # stop=["\n"]
    #     )
    #     # new = response['choices'][0]['text']
        
    #     new = response['choices'][0]['text']
    openai.api_key=settings.OPENAI_KEY

    keep_prompting=True
    while keep_prompting:
        prompt=msg
        if prompt=='exit':
            keep_prompting=False
        else:
            response=openai.Completion.create(engine='text-davinci-003',prompt=msg,max_tokens=200)
            return HttpResponse(json.dumps(response), content_type="application/json")

    else:
        response = {'error': 'OpenAI key not configured'}
    return HttpResponse(json.dumps(response), content_type="application/json")
    # return HttpResponse(json.dumps(new),content_type='application/json')
    
