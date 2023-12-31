from django.db import models

# Create your models here.


# photo, 

class first_display(models.Model):
    firstimage = models.ImageField(upload_to="profile" ,blank=True)
    displayname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)





class about(models.Model):
    aboutphoto = models.ImageField(upload_to="about/profile", blank=True)
    aboutdetail = models.CharField(max_length=150 ,)
    age = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    work = models.CharField(max_length=150)
    
    
    freelance = models.CharField(max_length=150)
    freelance_project = models.CharField(max_length=150,blank=True)

    freelance_num = models.CharField(max_length=150)
    
    
    
    # Experience = models.CharField(max_length=150)
    # Projects_Completed = models.CharField(max_length=150)
    # Happy_Clients = models.CharField(max_length=150)
    # Awards_Won = models.CharField(max_length=150)
    # age = models.CharField(max_length=150)
    

class aboutproject(models.Model):    
    Freelance_project = models.CharField(max_length=150,blank=True)

    Freelance_num = models.CharField(max_length=150,blank=True)



        #  My Skills
class My_Skills(models.Model):    
    MySkills = models.CharField(max_length=150,blank=True)
    percent = models.CharField(max_length=150,blank=True)
    width_percent = models.CharField(max_length=150,blank=True)

class My_Skills2(models.Model):    
    MySkills = models.CharField(max_length=150,blank=True)
    percent = models.CharField(max_length=150,blank=True)
    width_percent = models.CharField(max_length=150,blank=True)



                            # Qualification

class education(models.Model):    
    education_date = models.CharField(max_length=150,blank=True)
    education_name = models.CharField(max_length=150,blank=True)
    education_detail = models.CharField(max_length=150,blank=True)



                            # Qualification experience


class experience(models.Model):    
    experience_date = models.CharField(max_length=150,blank=True)
    experience_name = models.CharField(max_length=150,blank=True)
    experience_detail = models.CharField(max_length=150,blank=True)



                        # My Services

class MyServices(models.Model):    
    Servicespng = models.CharField(max_length=150,blank=True) 
    Services_name = models.CharField(max_length=150,blank=True)                        
    Services_detail = models.CharField(max_length=150,blank=True)                        
    


                        # My Portfolio
class Category(models.Model): 
    Services_name = models.CharField(max_length=150,blank=True) 





class MyPortfolio(models.Model):    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Portfolio = models.ImageField(upload_to="Services/png")

    Services_name = models.CharField(max_length=150,blank=True) 







                        # Testimonials









                        # My Blog


















                        # Contact Me


class contact_info(models.Model):
    GetInTouch = models.CharField(max_length=100,blank=True) 
    detail = models.CharField(max_length=100,blank=True) 


class Contact_detail(models.Model):
    name = models.CharField(max_length=100,blank=True) 
    Contacticon = models.CharField(max_length=150,blank=True)  
    Contact_social_mob = models.CharField(max_length=150,blank=True)  
    Contactiadd = models.CharField(max_length=150,blank=True)  




                        # Contact us

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)







                        # social media

class social_media(models.Model):
    social_icon = models.CharField(max_length=100,blank=True) 
    social_media_link = models.CharField(max_length=150,blank=True) 




class file(models.Model):
    pdf = models.FileField(upload_to='staticmedia')

