from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from blimp.users.api.views import UserViewSet
from blimp.specimen.api.views import (
    StudyViewSet,
    StudyParticipantViewSet,
    StorageLocationViewSet,
    BiospecimenViewSet,
)

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("studies", StudyViewSet)
router.register("participants", StudyParticipantViewSet)
router.register("storage-locations", StorageLocationViewSet)
router.register("specimens", BiospecimenViewSet)


app_name = "api"
urlpatterns = router.urls
