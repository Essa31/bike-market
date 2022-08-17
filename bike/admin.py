from django.contrib import admin

from .models import Bike
# Register your models here.


class CustomSnackAdmin(admin.ModelAdmin):
    model = Bike
    fieldsets = (
        ('Owner', {
            'fields' : ('purchaser',)
        }),
        ('Bike Info', {
            'fields':(
                'name',
                'desc'
            )
        })
    )

    list_display = ('name', 'purchaser')
    list_filter = ('name', 'desc')
    search_fields = ('name', 'desc')


admin.site.register(Bike, CustomSnackAdmin)