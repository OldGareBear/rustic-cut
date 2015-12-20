from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def to_json(self):
        return json.dumps(self.to_dict())