from django.db import models


class ResultGameInLive(models.Model):

    first_array_living_cells = models.IntegerField()
    iterations = models.IntegerField()
    next_array_living_cells = models.IntegerField()
    period_repetition_location = models.IntegerField()



