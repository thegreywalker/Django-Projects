from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january": "Its time for a Holiday!",
    "february": "Walk more 20 miles.",
    "march": "Summer Holiday",
    "april": "Warmth on it's Peak",
    "may": "Month after April fool",
    "june": "I am excited for a Monsoon",
    "july": "Here You go .. Time to Go !",
    "august": "Agust is here",
    "septembar": "My Birthday is in the House",
    "octobar": "It's End Before Beginning Part 1",
    "novembar": "It's Movembar. Menth's Health Matters.",
    "december": "End Before Beginning ... Final Chapter!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("Monthly_Challenge", args=[month])
        list_items += f"""<li>
        <h1>
            <a href=\"{month_path}\">{capitalized_month}</a>
        </h1>
        </li>"""
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("This Month is not Valid!")

    forward_month = months[month - 1]
    forward_path = reverse("Monthly_Challenge", args=[forward_month])
    return HttpResponseRedirect(forward_path)


def monthly_challenge(request, month):
    challenge_text = monthly_challenges[month]
    # return HttpResponse(challenge_text)
    return render(request, 'challenges/challenge.html', {
        "challenge_text": challenge_text
    })


