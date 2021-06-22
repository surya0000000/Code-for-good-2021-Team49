from django.contrib import admin
from .models import Profile,Complaint,Grievance, ScheduledMail, MailAttachment, MailRecipient

class CAdmin(admin.ModelAdmin):
    list_display = ('user','Subject','Type_of_complaint','Description','Time','status')

admin.site.register(Profile)
admin.site.register(Complaint,CAdmin)
admin.site.register(Grievance)

# for the scheduled mail
@admin.register(ScheduledMail)
class MailAdmin(admin.ModelAdmin):
	pass

@admin.register(MailAttachment)
class AttachmentAdmin(admin.ModelAdmin):
	pass

@admin.register(MailRecipient)
class RecipientAdmin(admin.ModelAdmin):
	pass