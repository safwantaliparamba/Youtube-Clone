from django.contrib import admin

from general.models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name","id","web_code","country_code","flag","phone_code","phone_number_length","is_active"]
    search_fields = ["name","phone_number_length","web_code","phone_code"]