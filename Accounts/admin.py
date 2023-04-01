from django.contrib import admin

from .models import CustomUser, Saved

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username','first_name','last_name', 'email', 'country', 'city', 'age', 'zipcode',
                    'phone_number','created_at', 'updated_at')
    list_filter = ['country', 'city', 'age', 'zipcode', 'created_at', 'updated_at']
    search_fields = ['username', 'phone_number']


admin.site.register(Saved)