from cgitb import html
from operator import index
from django.shortcuts import render
from .models import Bmi
from math import pi

# Create your views here.
def home(request ):
    context = { }
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))
            age = int(request.POST.get("age-metric")
            )
            gender = chr(request.POST.get("gender-metric"))
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial"))/2.205
            height = (float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100

        bmi = (weight/(height**2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(user=request.user,weight=weight, height=height, age=age, gender = gender, bmi=round(bmi))


    # do chnages in this

        # if bmi < 16:
        #      state = "Severe Thinness"
        # elif bmi > 16 and bmi < 17:
        #     state = "Moderate Thinness"
        # elif bmi > 17 and bmi < 18:
        #     state = "Mild Thinness"
        # elif bmi > 18 and bmi < 25:
        #     state = "Normal"
        # elif bmi > 25 and bmi < 30:
        #     state = "Overweight"
        # elif bmi > 30 and bmi < 35:
        #     state = "Obese Class I"
        # elif bmi > 35 and bmi < 40:
        #     state = "Obese Class II"
        # elif bmi > 40:
        #     state = "Obese Class III"
            

        context["bmi"] = round(bmi)
        context["state"] = state

    if request.user.is_authenticated:
        bmis = []
        num = 1
        dates_queryset = Bmi.objects.all().filter(user = request.user)
        for qr in dates_queryset:
            bmis.append(int(qr.bmi))
            num += 1
        # add a step renderer
        
        context["script"] = script
        context["div"] = div

    return render(request, "bmi/index1.html", context)
    return render(request, "bmi/index2.html", context)

