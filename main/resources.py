from import_export import resources
from .models import Finance

class FinanceResource(resources.ModelResource):

    class Meta:
        model = Finance