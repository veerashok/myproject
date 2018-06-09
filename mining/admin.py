from django.contrib import admin
from .models import MiningInput, Stages, StagesWiseCost


class AdminSatges(admin.ModelAdmin):
    list_display = ('processing_cost','stage_number')


admin.site.register(Stages, AdminSatges)


class AdminMiningInput(admin.ModelAdmin):
    list_display = ('name', 'cost', 'stage')


admin.site.register(MiningInput, AdminMiningInput)


def computed_values(obj):
    list_mininginputs = MiningInput.objects.all()
    list_stages = Stages.objects.all()

    my_final_cost = StagesWiseCost()

    existing_stages = []

    for obj1 in list_stages:
        existing_stages.append(obj1.stage_number)
        #print(obj1.stage_number)

    for obj1 in list_stages:
        my_final_cost.stage = obj1.stage_number
        my_final_cost.computed_cost = obj1.processing_cost
        my_final_cost.save()

    for obj2 in list_mininginputs:

        temp1 = (list(StagesWiseCost.objects.filter(pk = obj2.stage).values()))
        current_cost = temp1[0]['computed_cost']
        current_cost += obj2.cost

        StagesWiseCost.objects.filter(pk=obj2.stage).update(computed_cost=current_cost)


class AdminStageWiseCost(admin.ModelAdmin):
    list_display = ('stage','computed_cost', computed_values)


admin.site.register(StagesWiseCost, AdminStageWiseCost)

