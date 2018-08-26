from .models import Product
from haystack import indexes
import datetime


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    author = indexes.CharField(model_attr='user')

    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
