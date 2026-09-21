from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from functools import wraps
from django.conf import settings

from main.models import Experience, Education, Skill, Project
from main.forms import ProjectForm, ExperienceForm, EducationForm, SkillForm

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get("is_admin"):
            messages.error(request, "Anda harus masuk ke mode admin untuk melakukan aksi ini!")
            return redirect("main:edit_login")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def edit_login(request):
    if request.method == "POST":
        password = request.POST.get("password", "")
        if password == settings.ADMIN_PASSWORD:
            request.session["is_admin"] = True
            messages.success(request, "Berhasil masuk ke mode edit!")
            return redirect("main:show_main")
        else:
            messages.error(request, "Password salah!")

    return render(request, "login.html", {"name": "Ranu Ario Sulistianto"})


def edit_logout(request):
    request.session.flush()
    messages.success(request, "Berhasil keluar dari mode edit.")
    return redirect("main:show_main")

# main ================================================================================================================
def show_main(request):
    context = {
        "name": "Ranu Ario Sulistianto",
        "npm": "2506657270",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at the University of Indonesia with a strong passion for technology, "
            "programming, and business. Highly motivated to continuously learn and apply innovative solutions. "
            "Eager to contribute through hands-on experience while developing expertise in programming, "
            "communication, project management, and collaborative teamwork."
        ),
    }
    return render(request, "index.html", context)


# project ============================================================================================================
@admin_required
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Ranu Ario Sulistianto",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

@admin_required
def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@admin_required
def update_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


# experience =========================================================================================================
def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]

    context = {
        "name": "Ranu Ario Sulistianto",
        "experience_list": experiences,
    }
    return render(request, "experience.html", context)

@admin_required
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@admin_required
def update_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@admin_required
def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Data pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_experience_json(request):
    experiences = Experience.objects.all()
    data = serializers.serialize("json", experiences)
    return HttpResponse(data, content_type="application/json")


# education ==========================================================================================================
def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [edu.object for edu in educations]
    
    context = {
        "name": "Ranu Ario Sulistianto",
        "educations": educations,
    }
    return render(request, "education.html" , context)

@admin_required
def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
    }
    return render(request, "education_form.html", context)

@admin_required
def update_education(request, id):
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)

@admin_required
def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Data pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def get_education_json(request):
    educations = Education.objects.all().order_by('-start_year')
    data = serializers.serialize("json", educations)
    return HttpResponse(data, content_type="application/json")


# skill ============================================================================================================
def show_skills(request):
    json_response = get_skills_json(request)
    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]

    context = {
        "name": "Ranu Ario Sulistianto",
        "skills": skills,
    }
    return render(request, "skills.html", context)

@admin_required
def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
    }
    return render(request, "skills_form.html", context)

@admin_required
def update_skill(request, id):
    skill = get_object_or_404(Skill, pk=id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill berhasil diperbarui!")
        return redirect("main:show_skills")

    context = {
        "name": "Ranu Ario Sulistianto",
        "form": form,
        "skill": skill,
    }
    return render(request, "skills_form.html", context)

@admin_required
def delete_skill(request, id):
    skill = get_object_or_404(Skill, pk=id)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")

def get_skills_json(request):
    skills = Skill.objects.all()
    data = serializers.serialize("json", skills)
    return HttpResponse(data, content_type="application/json")