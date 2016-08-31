from django.contrib import admin
from .models import Product, ProductBacklogItem, Sprint, AceptanceRequirement, Activity

class PBItemInline(admin.TabularInline):
    model = ProductBacklogItem
    extra = 0
class ProductAdmin(admin.ModelAdmin):
    inlines = [PBItemInline]
    search_fields = ['name']

class AceptanceRequirementInline(admin.TabularInline):
    model = AceptanceRequirement
    extra = 0
class ProductBacklogItemAdmin(admin.ModelAdmin):
    inlines = [AceptanceRequirementInline]

    list_display = ['title', 'estimations', 'status']
    search_fields = ['title']
    list_filter = ['status', 'estimations']

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0
class SprintAdmin(admin.ModelAdmin):
    inlines = [ActivityInline]

    list_display = ['id', 'description', 'status']
    list_filter = ['status', ]

admin.site.register(Product, ProductAdmin)
#admin.site.register(EstimationsPBitems)
admin.site.register(ProductBacklogItem, ProductBacklogItemAdmin)
admin.site.register(Sprint, SprintAdmin)