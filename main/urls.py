from django.urls import path

from main.views import (
    show_main,
    register,
    login_user,
    logout_user,
    toggle_star,
    # project
    show_projects,
    create_project,
    create_project_ajax,
    update_project,
    delete_project,
    delete_project_ajax,
    get_projects_json,
    # education
    show_education,
    create_education,
    create_education_ajax,
    update_education,
    delete_education,
    delete_education_ajax,
    get_education_json,
    # experience
    show_experience,
    create_experience,
    create_experience_ajax,
    update_experience,
    delete_experience,
    delete_experience_ajax,
    get_experience_json,
    # skill
    show_skills,
    create_skill,
    create_skill_ajax,
    update_skill,
    delete_skill,
    delete_skill_ajax,
    get_skills_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),

    # experience
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:id>/delete-ajax/", delete_experience_ajax, name="delete_experience_ajax"),

    # education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:id>/edit/", update_education, name="update_education"),
    path("education/<uuid:id>/delete/", delete_education, name="delete_education"),
    path("education/<uuid:id>/delete-ajax/", delete_education_ajax, name="delete_education_ajax"),

    # skills
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skill, name="create_skill"),
    path("skills/add-ajax/", create_skill_ajax, name="create_skill_ajax"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("skills/<uuid:id>/edit/", update_skill, name="update_skill"),
    path("skills/<uuid:id>/delete/", delete_skill, name="delete_skill"),
    path("skills/<uuid:id>/delete-ajax/", delete_skill_ajax, name="delete_skill_ajax"),

    # projects
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:id>/edit/", update_project, name="update_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:id>/delete-ajax/", delete_project_ajax, name="delete_project_ajax"),

]