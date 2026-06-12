from django.contrib import admin
from .models import (
    GeneralSetting,
    Profile,
    Experience,
    Project,
    Education,
    Interest,
    SkillCategory,
    Skill,
    Language,
    AwsBadge,
    Certificate,
    ContactMessage,
)


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parameter')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'phone', 'location')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'period', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('company', 'role', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'technologies', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'technologies', 'description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'faculty', 'department')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_highlighted', 'order')
    list_editable = ('is_highlighted', 'order')
    list_filter = ('category',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'order')
    list_editable = ('order',)


@admin.register(AwsBadge)
class AwsBadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('organization', 'title', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date', 'is_read')
    list_filter = ('is_read', 'created_date')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_date',)