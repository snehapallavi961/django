from studentapi.viewsets import StudentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student',StudentViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive