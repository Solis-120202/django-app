from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class client(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=False)
    password = models.CharField(max_length=128, null=False, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)    

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name


class product(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name


class ClientProduct(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(product, on_delete=models.CASCADE, default=None)
    account_number = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.client.name} - {self.product.name}"


class transaction_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=3, null=False)
    description = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(client, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(product, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name


class transaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(product, on_delete=models.CASCADE, default=None)
    
    transaction_type = models.ForeignKey(
        transaction_type,
        on_delete=models.CASCADE,
        related_name="transactions",
        default=None,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return (
            f"{self.client.name} - {self.product.name} - {self.transaction_type.name}"
        )