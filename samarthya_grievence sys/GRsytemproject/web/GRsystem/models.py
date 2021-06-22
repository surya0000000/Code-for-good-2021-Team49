from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator
from datetime import datetime, date
from django.utils import timezone

from django.conf import settings
from django.core.mail import EmailMessage
class Meta:

    app_label = 'GRsystem'
class Profile(models.Model):
    typeuser =(('SMC Member','SMC Member'),('grievance', 'grievance'))
    # COL=(('GPS Piau Muniyari','GPS Piau Muniyari'),('GPS Piau Muniyari','GPS Piau Muniyari')) #change college names
    user =models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    schoolname=models.CharField(max_length=1000, blank=False)
    phone_regex =RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format:Up to 10 digits allowed.")
    contactnumber = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    type_user=models.CharField(max_length=20,default='student',choices=typeuser)
    schoolid=models.CharField(max_length=20)
    def __str__(self):
        return self.collegename
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('Infrastructure',"Infrastructure"),('Human Resources',"Human Resources"),('Management',"Management"),('Other',"Other"))
    
    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Receiver = models.CharField(max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)

class Grievance(models.Model):
    guser=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return str(self.guser)


# for sending emails
auto_mail_from = 'sakshamb117@gmail.com'
if hasattr(settings, 'AUTO_MAIL_FROM'):
	auto_mail_from = settings.auto_mail_from
class MailAttachment(models.Model):
	attachment_file = models.FileField()
	attached_to = models.ForeignKey('ScheduledMail', related_name = 'attachments', on_delete = models.CASCADE)

	def __str__(self):
            return '%s (%s)' % (self.attachment_file.filename, self.attached_to.subject)


class MailRecipient(models.Model):
	mail_address = models.CharField(max_length = 40)

	def __str__(self):
    	    return self.mail_address



class ScheduledMail(models.Model):
	subject = models.CharField(max_length = 40)
	template = models.FileField(upload_to = 'mail_app/mails')
	send_on = models.DateTimeField()
	recipients_list = models.ManyToManyField(MailRecipient, related_name = 'mail_list')

	def __str__(self):
    	    return self.subject
    
    
