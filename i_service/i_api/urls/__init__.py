from . import job
# from . import device
# from . import city
# from . import event
# from . import group
# from . import ws
from . import account



urlpatterns = [
    *account.urlpatterns,
    *job.urlpatterns
]
