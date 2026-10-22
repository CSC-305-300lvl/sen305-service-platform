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