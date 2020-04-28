from django.db import models

class Specimen(models.Model):
    '''Models all specimens currently available in the inventory.'''
    c_name=models.TextField(blank=False)
    category=models.TextField(blank=False)
    image=models.TextField(blank=False)
    kingdom=models.TextField(blank=False)
    phylum=models.TextField(blank=False)
    classs=models.TextField(blank=False)
    order=models.TextField(blank=False)
    family=models.TextField(blank=False)
    genus=models.TextField(blank=False)
    species=models.TextField(blank=False)
    s_species=models.TextField(blank=True)
    def is_taken(self):
        return Check.objects.filter(specimen=self)

    def __str__(self):
        '''Return a string representation of specimen.'''
        return '%s' %(self.c_name)

class Individual(models.Model):
    '''Models individuals registered in system to check out.'''
    name=models.TextField(blank=False,null=False)
    email=models.TextField(blank=False,null=False)
    department=models.TextField(blank=True,null=False)
    def __str__(self):
        '''Return a string representation of individual.'''
        return '%s (%s), %s department' %(self.name, self.email, self.department)

class Check(models.Model):
    '''Models a record of specimens taken out.'''
    checkout=models.DateField(auto_now_add=False)
    checkin=models.DateField(auto_now_add=False)
    specimen=models.ForeignKey(Specimen, on_delete=models.CASCADE)
    individual=models.ForeignKey(Individual, on_delete=models.CASCADE)
    def get_all(self):
        return list(Check.objects.all())
    def __str__(self):
        '''Return a string representation of checkout.'''
        return '%s: %s reserved by %s In: %s Out: %s' %(self.pk, self.specimen, self.individual, self.checkout, self.checkin)