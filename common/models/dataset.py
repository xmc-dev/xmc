from django.db import models
from django.utils.translation import ugettext_lazy as _

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    # stdin if empty
    input_file = models.CharField("input file name. If empty, it's stdin", max_length=200, blank=True)
    # stdin if empty
    output_file = models.CharField("output file name. If empty, it's stdout", max_length=200, blank=True)
    time_limit = models.DurationField()
    memory_limit = models.PositiveIntegerField("memory limit in bytes")

class TestCase(models.Model):
    input_data = models.TextField()
    output_data = models.TextField()
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
