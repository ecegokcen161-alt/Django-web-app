from django.db import models


class GeneralSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)
    parameter = models.CharField(max_length=255, default='', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.company


class Project(models.Model):
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=100, blank=True)
    technologies = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    campus = models.CharField(max_length=200, blank=True)
    badge = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.school


class Interest(models.Model):
    icon = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Skill categories'

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField(max_length=100)
    is_highlighted = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class AwsBadge(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Certificate(models.Model):
    organization = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name