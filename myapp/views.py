from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from myapp.models import CourseDetail, Contact,Affiliation

def index(request):
    courses = CourseDetail.objects.all()
    return render(request, 'index.html', {"courses": courses})

def about(request):
    return render(request, 'about.html')

def affiliations(request):
    data = Affiliation.objects.all()
    return render(request, 'affiliation.html', {'affiliations': data})

def contact(request):
    return render(request, 'contact_us.html')

def contact_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Optional success message
        messages.success(request, 'Your message has been sent successfully!')

        # Redirect to contact page
        return redirect('contact')

    # If not POST, redirect to contact page
    return redirect('contact')

def course(req):
    courses = CourseDetail.objects.all()
    return render(req,'course.html',{"courses": courses})
def course_detail(request, course_id):
    course = get_object_or_404(CourseDetail, id=course_id)
    return render(request, 'course_detail.html', {'course': course})
