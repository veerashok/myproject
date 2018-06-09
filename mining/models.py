from django.db import models


class Stages(models.Model):
    stage_number = models.IntegerField(primary_key=True)
    processing_cost = models.IntegerField()


class MiningInput(models.Model):
    stages = models.ForeignKey(Stages, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False, default=0)
    cost = models.IntegerField(default=0)
    stage = models.IntegerField(default=0)


class StagesWiseCost(models.Model):
    stage = models.IntegerField(primary_key=True)
    computed_cost = models.IntegerField(default=0)

