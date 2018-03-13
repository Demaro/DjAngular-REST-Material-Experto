from django.apps import AppConfig
from django.contrib import admin

from .models import Ticket, Status


class TicketModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description" ,"slug", "createdAt", "updatedAt", "user", "status"]
	list_display_links = ["slug"]
	list_editable = ["description", "name"]
	list_filter = ["status","user"]

	search_fields = ["name", "slug", "user",]
	class Meta:
		model = Ticket


admin.site.register(Ticket, TicketModelAdmin)

class StatusModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", ]
	list_display_links = ["id"]


	search_fields = ["name",]
	class Meta:
		model = Status


admin.site.register(Status, StatusModelAdmin)






