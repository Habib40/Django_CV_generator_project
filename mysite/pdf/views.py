from django.shortcuts import render,HttpResponse ,redirect
from .models import Profile
import pdfkit
from django.template import loader
import io
# Create your views here.
import logging

def index(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summery = request.POST.get('summery')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        skills = request.POST.get('skills')
        previouse_work = request.POST.get('previouse_work')

        # Log received values for debugging
        logging.debug(f'Received data - Name: {name}, Email: {email}, Phone: {phone}, Summary: {summery}')

        # Validate required fields
        if name and email and phone and summery:  # Ensure required fields are filled
            # Create profile instance
            profile = Profile(
                name=name,
                email=email,
                phone=phone,
                summery=summery,
                degree=degree,
                school=school,
                university=university,
                skills=skills,
                previouse_work=previouse_work,
            )
            profile.save()
            return redirect('list')  # Redirect to a success page or another view
        else:
            error_message = 'Please fill in all required fields.'
            return render(request, 'pdf/accept.html', {'error': error_message})

    return render(request, 'pdf/accept.html')

def Resume(request,id):
    profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'profile':profile})
    options = {
    'page-size': 'Letter',  
    'encoding': 'UTF-8'
    }
    
    
    pdf = pdfkit.from_string(html,False,options)
    respones = HttpResponse(pdf,content_type='application/pdf')
    respones['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return respones

def Profile_list(request):
    profiles = Profile.objects.all().order_by('-created_date')
    return render(request,'pdf/profile.html',{'profiles':profiles})