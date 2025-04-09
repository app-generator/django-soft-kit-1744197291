# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Section(models.Model):

    #__Section_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    #__Section_FIELDS__END

    class Meta:
        verbose_name        = _("Section")
        verbose_name_plural = _("Section")


class Testcase(models.Model):

    #__Testcase_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    #__Testcase_FIELDS__END

    class Meta:
        verbose_name        = _("Testcase")
        verbose_name_plural = _("Testcase")


class Testcasestep(models.Model):

    #__Testcasestep_FIELDS__
    number = models.IntegerField(null=True, blank=True)
    instructions = models.TextField(max_length=255, null=True, blank=True)
    expectations = models.TextField(max_length=255, null=True, blank=True)
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    #__Testcasestep_FIELDS__END

    class Meta:
        verbose_name        = _("Testcasestep")
        verbose_name_plural = _("Testcasestep")


class Testsuite(models.Model):

    #__Testsuite_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    #__Testsuite_FIELDS__END

    class Meta:
        verbose_name        = _("Testsuite")
        verbose_name_plural = _("Testsuite")



#__MODELS__END
