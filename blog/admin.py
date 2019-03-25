from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 指定数据列表展示页面可以显示的字段
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    # 指定添加页面上有哪些字段可以显示。
    fields = ('name', 'status', 'is_nav',)

    def save_model(self, request, obj, form, change):
        """
        重写save_model方法
        :param request: Django封装的request请求
        :param obj: 当前数据对象
        :param form: 用户提交过来的表单之后的对象
        :param change: 用于标志本次保存的数据是新增的还是更新的。
        :return:
        """
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):

    list_display = ['name', 'status', 'created_time']
    fields = ['name', 'status']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'status',
        'created_time',
        'operator'
    )
    # 用来配置哪些字段可以作为链接来配置它们，直接点击就可以进入编辑界面了。
    list_display_links = []

    # 配置页面过滤器，可以通过哪些字段来过滤列表页
    list_filter = ['category']

    # 配置搜索字段
    search_fields = ['title', 'category__name']

    # Action相关的操作是否展示在顶部或者底部
    actions_on_top = True
    actions_on_bottom = True

    # 保存，编辑，编辑并新建按钮是否在顶部展示
    save_on_top = True

    fields = (
        # 这样写到一个元组里它会把这俩内容放到一行去显示
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    # 自定义函数，参数固定，obj就是当前行的对象
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id, ))
        )

    # 指定表头字段名称
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)




