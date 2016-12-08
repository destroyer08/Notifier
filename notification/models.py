from django.db import models
from django.contrib.auth.models import User

# Creating a model for data which is frequently changable by admin
class Stock(models.Model):
    stock_name = models.CharField(max_length = 128)
    price = models.FloatField(default=0)
    subscriber = models.ManyToManyField(User)

    def __unicode__(self):  
        return self.stock_name

# creating a model which saves logs containing all changes done by admin
class NotificationLogs(models.Model):
	user = models.ForeignKey(User)
	stock = models.ForeignKey(Stock)
	stock_price = models.FloatField(default = 0)
	timestamp = models.DateTimeField(auto_now_add=True)


   	def __unicode__(self):
   		return unicode(self.stock.stock_name)



