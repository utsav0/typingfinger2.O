import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
import csv
import random  # For generating words


def home(request):
    return render(request, "index.html")


# This generate random text:


def generateTxt(request):
    charList = []
    # Getting the csv file path:
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, "words.csv")

    with open(file_path, "r") as fh:
        fhReader = list(csv.reader(fh))  # Getting all the words from CSV file

        # Choosing 10 random words:
        wordList = random.choices(list(fhReader[0]), k=10)

        # Splitting the words into characters:
        for word in wordList:
            charList.append([char for char in word])
        return JsonResponse(charList, safe=False)


# For result page:
def result(request):
    return render(request, "result.html")

# When clicked on retry button
def practiceAgain(request):
    return render(request, "index.html")
