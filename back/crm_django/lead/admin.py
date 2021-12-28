from django.contrib import admin
from .models import Lead
# Register your models here.
#admin.site.register(Lead)
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('company','contact_person','email','status','priority','created_by',)



