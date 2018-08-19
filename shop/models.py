# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='分类名称')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='分类URL')

    class Meta:
        ordering = ('-name',)
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='分类')
    size = models.CharField(max_length=200, db_index=True, verbose_name='商品大小')
    name = models.CharField(max_length=200, db_index=True, verbose_name='商品名称')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='商品URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='商品图片')
    description = models.TextField(blank=True, verbose_name='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    stock = models.PositiveIntegerField(verbose_name='商品库存')
    available = models.BooleanField(default=True, verbose_name='是否可购买')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
