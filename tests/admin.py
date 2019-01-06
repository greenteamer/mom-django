from django.contrib import admin
from django import forms
from .models import Test, TestQuestion, TestQuestionVariant, StudentTest, StudentTestAnswer
import nested_admin


class TestQuestionVariantNested(nested_admin.NestedTabularInline):
    model = TestQuestionVariant
    classes = ('grp-collapse grp-open',)


class TestQuestionInline(nested_admin.NestedTabularInline):
    model = TestQuestion
    inlines = [TestQuestionVariantNested, ]
    classes = ('grp-collapse grp-open',)


class TestAdmin(nested_admin.NestedModelAdmin):
    model = Test
    # list_display = ['name', 'slug', 'created', 'last_updated', 'text']
    readonly_fields = ['created', 'last_updated']
    fieldsets = (
        (None, {
            'fields': ()
        }),
        ('Основная информация', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('name', 'text', ),
        }),
    )
    inlines = [
        TestQuestionInline,
    ]

admin.site.register(Test, TestAdmin)


class TestQuestionVariantInline(admin.TabularInline):
    model = TestQuestionVariant


class TestQuestionAdminForm(forms.ModelForm):

    class Meta:
        model = TestQuestion
        fields = '__all__'


class TestQuestionAdmin(admin.ModelAdmin):
    form = TestQuestionAdminForm
    list_display = ['name', 'text', 'points']
    inlines = [TestQuestionVariantInline, ]

admin.site.register(TestQuestion, TestQuestionAdmin)


class TestQuestionVariantAdminForm(forms.ModelForm):

    class Meta:
        model = TestQuestionVariant
        fields = '__all__'


class TestQuestionVariantAdmin(admin.ModelAdmin):
    form = TestQuestionVariantAdminForm
    list_display = ['name', 'value']

admin.site.register(TestQuestionVariant, TestQuestionVariantAdmin)


class StudentTestAdminForm(forms.ModelForm):

    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentTestAdmin(admin.ModelAdmin):
    form = StudentTestAdminForm
    list_display = ['totalPoints']

admin.site.register(StudentTest, StudentTestAdmin)


class StudentTestAnswerAdminForm(forms.ModelForm):

    class Meta:
        model = StudentTestAnswer
        fields = '__all__'


class StudentTestAnswerAdmin(admin.ModelAdmin):
    form = StudentTestAnswerAdminForm


admin.site.register(StudentTestAnswer, StudentTestAnswerAdmin)


