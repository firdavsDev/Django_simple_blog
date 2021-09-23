from django.db import models
from django.urls import reverse

# Create your models here.

#Bazani shu rosim orqali yaratib olishimiz mumkin faqat model faylida 
class Product(models.Model):
    title=models.CharField(max_length=50) #bu talab qiladi max_lengthni
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10000)
    summary=models.TextField(blank=False,null=False)
    sale = models.BooleanField(default=True)

    #bu linklarni uzgartirib beradi 1
    # def get_absoulte_url(self):
    #     return f"/product/{self.id}"

    #bu linklarni uzgartirib beradi 2 usul
    def get_absoulte_url(self):
        #reverse 1chi argumenti bu urls dagi name ga teng
        return reverse('Product_list',kwargs={"id":self.id})