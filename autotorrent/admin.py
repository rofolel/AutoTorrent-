from django.contrib import admin

from autotorrent.models import episode, film,serie,actor


admin.site.register(episode)
admin.site.register(film)
admin.site.register(actor)
admin.site.register(serie)


