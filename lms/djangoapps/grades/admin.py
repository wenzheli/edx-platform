"""
Django admin page for grades models
"""
from config_models.admin import ConfigurationModelAdmin, KeyedConfigurationModelAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from lms.djangoapps.grades.config.forms import CoursePersistentGradesAdminForm
from lms.djangoapps.grades.config.models import (
    ComputeGradesSetting,
    CoursePersistentGradesFlag,
    PersistentGradesEnabledFlag
)
from lms.djangoapps.grades.models import PersistentSubsectionGradeOverride


class CoursePersistentGradesAdmin(KeyedConfigurationModelAdmin):
    """
    Admin for enabling subsection grades on a course-by-course basis.
    Allows searching by course id.
    """
    form = CoursePersistentGradesAdminForm
    search_fields = ['course_id']
    fieldsets = (
        (None, {
            'fields': ('course_id', 'enabled'),
            'description': 'Enter a valid course id. If it is invalid, an error message will display.'
        }),
    )


class PersistentSubsectionGradeOverrideAdmin(admin.ModelAdmin):
    list_display = ['get_course_id', 'earned_all_override', 'earned_graded_override', 'created', 'modified']
    search_fields = ['grade__course_id']

    def get_course_id(self, persistent_grade):
        return persistent_grade.grade.course_id

    get_course_id.short_description = _('Course Id')


admin.site.register(CoursePersistentGradesFlag, CoursePersistentGradesAdmin)
admin.site.register(PersistentGradesEnabledFlag, ConfigurationModelAdmin)
admin.site.register(ComputeGradesSetting, ConfigurationModelAdmin)
admin.site.register(PersistentSubsectionGradeOverride, PersistentSubsectionGradeOverrideAdmin)
