from django.contrib import admin
from .models import Choice, Question
# from .models import Question


# 你需要遵循以下流程——创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register() ——在你需要修改模型的后台管理选项时这么做。
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# 这里定义了ChoiceInline , 会展示已有的已经定义的Choice, 然后会有Extra的Choice给你添加 (其实没有这个extra也可以自己添加)
# 这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”
# 下面这种写法占据了大量的空间, 更改一下:
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 这在只有两个字段时显得没啥卵用，但对于拥有数十个字段的表单来说，为表单选择一个直观的排序方法就显得你的针很细了。
# 说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集：
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question text',    {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # 有了这个, Question Display就不单单展示question_text了, 还有对应的Date_published, was published recently字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

# 这样register显得比较凌乱，因为choice没有显示对应的Question，那么你点进去还需要选择对应的Question，不高效
# admin.site.register(Choice)

# 通过 admin.site.register(Question) 注册 Question 模型，Django 能够构建一个默认的表单用于展示。
# 通常来说，你期望能自定义表单的外观和工作方式。你可以在注册模型时将这些设置告诉 Django。
# admin.site.register(Question)