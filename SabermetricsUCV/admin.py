from django.contrib import admin

from .models import Pitching, Batting, Fielding


class PitchingLook(admin.ModelAdmin):
    fieldsets = (
        ('Equipo', {
            'fields': ['season', 'team']
        }),
        ('Atomicas', {
            'fields': ['w', 'l', 'era', 'g', 'gs', 'cg', 'sho', 'sv', 'ip', 'tbf', 'h', 'r', 'er', 'hr', 'bb', 'ibb',
                       'hbp', 'wp', 'so', 'lob'],
            'classes': ['collapse']
        }),
        ('Sabermetricas', {
            'fields': ['avg', 'whip', 'babip', 'fip', 'rar', 'war'],
            'classes': ['collapse']
        })
    )

    list_display = ('season', 'team')
    list_filter = ['season', 'team']
    search_fields = ['season', 'team']


admin.site.register(Pitching, PitchingLook)
admin.site.register(Batting)
admin.site.register(Fielding)




