from django.contrib import admin

from .models import Vehicle,Brand




class BrandInLine(admin.TabularInline):
    model = Brand
    extra = 3
class VehicleAdmin(admin.ModelAdmin):

    list_display = ('vehicle_type', 'release_date', 'was_released_recently')

    fieldsets = [ ('Vehicle Information', {'fields' : ['vehicle_type']}),
                  ('Date information', {'fields': ['release_date']}),
    ]
    inlines = [BrandInLine]
    list_filter = ['release_date']
    search_fields = ['vehicle_type']

admin.site.register(Vehicle, VehicleAdmin)
