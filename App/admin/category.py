from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")#выводится в таблице в админ панели(все в виде строк с наименованием поля модели)
    search_fields = ("name",)