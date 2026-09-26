from django.urls import path

from main.views import register, login_user, logout_user, show_main, show_experience, show_interest, get_interest_json, create_interest, delete_interest, edit_interest, show_education, create_project, show_project, get_projects_json, delete_project, toggle_star, toggle_star_interest

app_name = "main"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('interest/', show_interest, name='show_interest'),
    path('interest/add/', create_interest, name='create_interest'),    
    path("interest/<uuid:interest_id>/interest/",delete_interest,name="delete_interest"),
    path("interest/<uuid:interest_id>/edit_interest/",edit_interest,name="edit_interest"),
    path('education/', show_education, name='show_education'),
    path("api/interests/", get_interest_json, name="get_interests_json"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_project, name="show_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",),
    path("interest/<uuid:interest_id>/star/",toggle_star_interest,name="toggle_star_interest",),    
]
