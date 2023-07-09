from django.contrib import admin

class SupCardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rating", "contacts", "created_at")#выводится в таблице в админ панели(все в виде строк с наименованием поля модели)
    search_fields = ("name", "address")