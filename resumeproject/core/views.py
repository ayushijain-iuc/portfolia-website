from django.shortcuts import render
from . models import contactmodel
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def home(request):
    return render(request,"core/home.html")

def services(request):
    return render(request,'core/services.html')

def skills(request):
    return render(request,'core/skills.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

  
        if len(phone) != 10 or not phone.isdigit():
            return render(request, 'core/contact.html', {'error_message': 'Please enter a valid 10-digit phone number'})

        
        try:
            existing_entry = contactmodel.objects.get(email=email)
            return render(request, 'core/contact.html', {'error_message': 'Email already exists I Can Contact You As Soon As Possible'})
        except contactmodel.DoesNotExist:
            pass

        obj = contactmodel(name=name, email=email, phone=phone, message=message,subject=subject)
        
        try:
            obj.save()
            user_email = obj.email
            email_body = f"User Email: {user_email}\nUser Phone: {phone}\n\nMessage: {message}"
            email_subject = subject if subject else 'No subject' 
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='jainjainayushi111@gmail.com',  
                to=['jainjainayushi111@gmail.com'],  
                reply_to=[user_email], 
            )
            email.send()
            return render(request, 'core/contact.html', {'thankyou_message': 'Thank You To Contact Me'})
        except:
            return render(request, 'core/contact.html')
    
    return render(request, 'core/contact.html')


