from django.contrib import admin
from base.models import Azienda, Persona, Sede


def reset_notes(modeladmin, request, queryset):
    queryset.update(note=None)


reset_notes.short_description = "Resetta le note"


class PersonaAdmin(admin.ModelAdmin):
    list_filter = ["azienda"]
    list_display = ["nome", "cognome", "azienda", "email", "cf"]


class PersonaAdminInline(admin.TabularInline):
    model = Persona


class AziendaAdmin(admin.ModelAdmin):
    list_display = ["nome", "codice", "indirizzo", "citta"]
    list_filter = ["categoria_cliente"]
    search_fields = ["nome", "codice"]
    actions = [reset_notes]
    inlines = [PersonaAdminInline]



admin.site.register(Azienda, AziendaAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Sede)
