from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Ranu Ario Sulistianto",
        "npm": "2506657270",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at the University of Indonesia with a strong passion for technology, programming, and business. Highly motivated to continuously learn and apply innovative solutions. Eager to contribute through hands-on experience while developing expertise in programming, communication, project management, and collaborative teamwork."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ranu",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)