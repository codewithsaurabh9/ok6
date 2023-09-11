from django.shortcuts import render

from django.http import HttpResponse

from django.conf import settings


import os



from .models import first_display,about,aboutproject,My_Skills,My_Skills2,Contact_us,Category,MyPortfolio,education,experience,MyServices,contact_info,Contact_detail,social_media,file
# from .models import about,aboutproject
# from .models import first_display
# from .models import first_display


# Create your views here.

def index(request):
    if request.method =="POST":
        contact =Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
                )
        contact.save()

    okk = file.objects.all() 
    dis = first_display.objects.all()

    abo = about.objects.all()
    
    abopro = aboutproject.objects.all()
    skills = My_Skills.objects.all()
    Skills = My_Skills2.objects.all()
    Education = education.objects.all()

    Experience = experience.objects.all()
    myservices = MyServices.objects.all()
    Contact_info = contact_info.objects.all()
    contact_detail = Contact_detail.objects.all()
    Social_media = social_media.objects.all()
    # abo = about.objects.all()
   
    category = Category.objects.all()
    categoryId = request.GET.get('category')
    if categoryId:
        Products = MyPortfolio.objects.filter(category = categoryId)
    else:
        Products = MyPortfolio.objects.all()    
    auto1 = {
        'dis': dis,
        'abo': abo,
        'abopro': abopro,
        'skills': skills,
        'Skills': Skills,
        'category':category,
        'Products':Products,
        'Education':Education,
        'Experience':Experience,
        'myservices':myservices,
        'Contact_info':Contact_info,
        'contact_detail':contact_detail,
        'Social_media':Social_media,
        'okk':okk,
        # 'contact_detail':contact_detail,



    }
    
    #    print(user , orders)
    return render(request,'index.html',auto1)




def download(request):
    okk = file.objects.all() 
    # pdf = request.GET.get(okk)
    path = [okk]

    # path = "tmp/text.txt"
    # path = "tmp/SAURABH_MISHRA.pdf" 

    
    success = 2
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise "Http404"




