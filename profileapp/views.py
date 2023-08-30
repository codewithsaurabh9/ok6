from django.shortcuts import render

from django.http import HttpResponse

from django.conf import settings


import os



from .models import first_display,about,aboutproject,My_Skills,My_Skills2
# from .models import about,aboutproject
# from .models import first_display
# from .models import first_display


# Create your views here.

def index(request):


    dis = first_display.objects.all()

    abo = about.objects.all()
    
    abopro = aboutproject.objects.all()
    skills = My_Skills.objects.all()
    Skills = My_Skills2.objects.all()

    # abo = about.objects.all()
    # abo = about.objects.all()

    
    auto1 = {
        'dis': dis,
        'abo': abo,
        'abopro': abopro,
        'skills': skills,
        'Skills': Skills,



    }
    
    #    print(user , orders)
    return render(request,'index.html',auto1)




def download(request):
    # path = "tmp/text.txt"
    path = "tmp/SAURABH_MISHRA.pdf" 

    
    success = 2
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise "Http404"


