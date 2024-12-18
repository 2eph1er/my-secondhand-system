

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from baykeshop.public.tinymce import TinymceField
from baykeshop.public.abstract import AbstractModel, CategoryAbstractModel

User = get_user_model()


class BaykeArticleCategory(CategoryAbstractModel):
    """ 文章分类 """

    class Meta:
        ordering = ['-add_date']
        verbose_name = _('文章分类')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('baykeshop:article_category_detail', kwargs={'pk': self.pk})
    

class BaykeArticle(AbstractModel):
    """ 文章内容 """

    title = models.CharField(_("标题"), max_length=150)
    desc = models.CharField(_("描述"), max_length=200, blank=True, default="")
    keywords = models.CharField(_("关键字"), max_length=200, blank=True, default="")
    # content = models.TextField(_("内容"))
    content = TinymceField(_("内容"))
    category = models.ForeignKey(BaykeArticleCategory, on_delete=models.CASCADE, verbose_name=_("文章分类"))
    tags = models.ManyToManyField('BaykeArticleTags', blank=True, verbose_name=_("标签"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    
    # TODO: Define fields here

    class Meta:
        ordering = ['-add_date']
        verbose_name = _('文章')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('baykeshop:article_detail', kwargs={'pk': self.pk})
    
    @classmethod
    def get_archive(cls):
        return {date.strftime('%Y年%m月') for date in cls.objects.values_list('add_date', flat=True)}
    
    @classmethod
    def get_stats(cls, request, object_id):
        from baykeshop.module.stats.views import BaykeStatsMixins
        stats_cls = BaykeStatsMixins(request)
        stats = stats_cls.get_stats(cls, object_id)
        return stats
    
    
class BaykeArticleTags(AbstractModel):
    """ 文章标签 """

    name = models.CharField(_("名称"), max_length=50)
    
    # TODO: Define fields here

    class Meta:
        ordering = ['-add_date']
        verbose_name = _('文章标签')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('baykeshop:tags', kwargs={'pk': self.pk})
