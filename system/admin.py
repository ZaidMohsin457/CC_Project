from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse



admin.site.site_title = "DBMS"
admin.site.site_header = "Admin Panel"

class SpecificDateFilter(admin.SimpleListFilter):
    title = 'Specific Date'
    parameter_name = 'specific_date'

    def lookups(self, request, model_admin):
        # Get unique dates in a SQLite-compatible way
        queryset = ticket.objects.values_list('dest_pk__date', flat=True).order_by('dest_pk__date')
        # Use a set to get unique values
        unique_dates = set(queryset)
        return [(date.strftime('%Y-%m-%d'), date.strftime('%Y-%m-%d')) for date in unique_dates if date]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(dest_pk__date=value)
        return queryset

class ticketAdmin(admin.ModelAdmin):
    list_filter = (SpecificDateFilter, 'dest_pk__from_destination', 'dest_pk__to_destination',)
    search_fields = ('user_pk__username',)
    actions = ['export']

    def export(self, request, queryset):
        meta = self.model._meta
        fieldnames = [
            'Ticket Id','Reg No', 'First Name','Last Name',
            'From', 'To','Date','Time'
        ]
        from_destination = queryset.first().dest_pk.from_destination
        to_destination = queryset.first().dest_pk.to_destination
        filename = f'Tickets.{from_destination}-{to_destination}.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        writer = csv.writer(response)
        writer.writerow(fieldnames)

        for obj in queryset:
            row = writer.writerow([
                getattr(obj, 'pk'),
                getattr(obj.user_pk, 'username'),
                getattr(obj.user_pk, 'first_name'),
                getattr(obj.user_pk, 'last_name'),
                getattr(obj.dest_pk, 'from_destination'),
                getattr(obj.dest_pk, 'to_destination'),
                getattr(obj.dest_pk, 'date'),
                getattr(obj.dest_pk, 'time')
                
            ]) 

        return response
    export.short_description = "Download"   

class destAdmin(admin.ModelAdmin):
    radio_fields = {"to_destination": admin.HORIZONTAL,"from_destination": admin.HORIZONTAL}


# Register your models here.
admin.site.register(destination,destAdmin)
admin.site.register(ticket,ticketAdmin)
admin.site.register(driver)
