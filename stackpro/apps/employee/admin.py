from django.contrib import admin
from stackpro.apps.employee.models import advert, answer

class answerinline(admin.TabularInline):
	model = answer
	extra = 3
class advertadmin(admin.ModelAdmin):
	fieldsets = [
					(None,
					{'fields': ['status', 'avatar', 'titleofemployee', 'company', 'website', 'salary', 'place', 'prove', 'descriptionofjob', 'pub_date']}),
				]
	list_display = ('titleofemployee', 'company','salary', 'website', 'place','pub_date', 'status')
	list_filter = ['company']
	search_fields = ['company','titleofemployee']
	date_hierarchy = 'pub_date'
	inlines = [answerinline]

admin.site.register(advert, advertadmin)