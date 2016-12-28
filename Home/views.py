from django.shortcuts import render
from django.http import HttpResponse
from NeuralNetwork.deep_learner.train import *
from NeuralNetwork.deep_learner.featureVectorization import *

def index(request):
    return HttpResponse("Hello World")
