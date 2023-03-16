from django.contrib import admin

from users.models import User 

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","id","email","country","phone"]
    exclude = ["password","encrypted_password"]
    search_fields = ["username","phone"]