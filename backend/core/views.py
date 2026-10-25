from django.shortcuts import render


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "headline": "Report, track and resolve service requests",
            "active_requests": 0,
        },
    )


def about(request):
    project_roles = [
        "Requester",
        "Coordinator",
        "Technician",
        "Administrator",
    ]
    return render(
        request,
        "core/about.html",
        {"project_roles": project_roles},
    )


def contact(request):
    context = {
        "department_name": "Department of Software Engineering",
        "email": "servicedesk@veritas.edu.ng",
        "office_hours": "Monday to Friday, 9:00 AM - 4:00 PM",
    }
    return render(request, "core/contact.html", context)


def workflow(request):
    stages = [
        "Request submitted",
        "Request triaged",
        "Technician assigned",
        "Request resolved",
    ]
    return render(request, "core/workflow.html", {"stages": stages})