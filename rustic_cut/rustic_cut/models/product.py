import json

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=512)
    category = models.ForeignKey('Category', related_name='products')
    description = models.CharField(max_length=2096)
    photo = models.ImageField(upload_to='static/rustic_cut/img/product-photos', null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def to_json(self):
        return json.dumps(self.to_dict())