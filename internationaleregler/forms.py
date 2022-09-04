from django.forms import ModelForm
from internationaleregler.models import RacismPoint


class RacismPointForm(ModelForm):
    class Meta:
        model = RacismPoint
        fields = "__all__"