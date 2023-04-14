from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def index(request):
    if request.method == "POST":
        form_field = forms.AnalyserForm(request.POST, request.FILES)
        for k, v in request.POST.items():
            print(f"{k} : {v}")
        if form_field.is_valid():
            dish_path = form_field.cleaned_data["dest_file_path"]
            pofs = form_field.cleaned_data["parts_of_speech_field"]
            print(dish_path, pofs)
            return render(
                request,
                "chewer/index.html",
                {
                    "title": "CHEWER",
                    "form_field": form_field
                }
            )
        else:
            print(form_field.errors.as_data())
    form_field = forms.AnalyserForm(request.POST)
    return render(
        request,
        "chewer/index.html",
        {
            "title": "CHEWER",
            "form_field": form_field
        }
    )
