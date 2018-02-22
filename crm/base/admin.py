from django.contrib import admin
from base.models import Azienda


def reset_notes(modeladmin, request, queryset):
    queryset.update(note=None)


reset_notes.short_description = "Resetta le note"


class AziendaAdmin(admin.ModelAdmin):
    list_display = ["nome", "codice", "indirizzo", "citta"]
    list_filter = ["categoria_cliente"]
    search_fields = ["nome", "codice"]
    actions = [reset_notes]


admin.site.register(Azienda, AziendaAdmin)
