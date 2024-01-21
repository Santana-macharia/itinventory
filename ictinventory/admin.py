from django.contrib import admin
from .models import ITStaff
from .models import MohiUser
from .models import Centre
from .models import Department
from .models import Device
from .models import PPM


admin.site.register(ITStaff)
admin.site.register(MohiUser)
admin.site.register(Centre)
admin.site.register(Department)
admin.site.register(Device)
admin.site.register(PPM)



admin.site.site_header = 'Mohi IT Inventory'  # This will change the header text
admin.site.site_title = 'Mohi IT Inventory'    # This will change the browser tab title
admin.site.index_title = 'Mohi IT Inventory'   # This will change the main title on the admin index page
