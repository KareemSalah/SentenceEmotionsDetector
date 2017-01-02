from django.shortcuts import render
from django.http import HttpResponse
from NeuralNetwork.deep_learner.train import *
from NeuralNetwork.deep_learner.predict import *
from NeuralNetwork.deep_learner.featureVectorization import *
from numpy import array

def index(request):
    return render(request, 'home.html')

def train(request):
    vectorizer = FeatureVectorizer()
    vectorizer.start(mode='train', text=None)
    trainer = Trainer()
    acc = trainer.start()
    return HttpResponse(acc)

def predict(request):
    if 'textfile' in request.POST and 'textfile' not in request.FILES and len(request.POST['sentences']) == 0:
        return HttpResponse("NO DATA FOUND!")
    sentences = request.POST['sentences']
    if 'textfile' not in request.POST:
        textfile = request.FILES['textfile'].read().decode('utf-8')
    else:
        textfile = []

    all_sentences = []
    vectorizer = FeatureVectorizer()

    if len(sentences) != 0:
        for vector in vectorizer.start(mode='vectorize', text=sentences):
            all_sentences.append(vector)
    if len(textfile) != 0:
        for vector in vectorizer.start(mode='vectorize', text=textfile):
            all_sentences.append(vector)
    if len(all_sentences) == 0:
        return HttpResponse("NO DATA FOUND!")
    print 'seeeeeeeeeeeeeeee', all_sentences
    classifier = Classifier()
    result = classifier.start(all_sentences)

    return render(request, 'predict.html', {'result': result,
                                            'emo0': result['counters'][0],
                                            'emo1': result['counters'][1],
                                            'emo2': result['counters'][2]})
