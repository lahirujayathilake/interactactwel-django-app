from django.conf.urls import include
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

app_name = "interactwel"

router = routers.DefaultRouter()
router.register(r"subbasins", views.SubbasinViewSet, basename="subbasin")
router.register(r"users", views.UserViewSet, basename = "user")
router.register(r"roles", views.RoleViewSet, basename = "role")
router.register(r"groups", views.GroupViewSet, basename = "group")
router.register(r"grouproles", views.GroupRoleMappingViewSet, basename = "grouprole")
router.register(r"groupmembers", views.GroupMembershipViewSet, basename = "groupmember")

router.register(r"events", views.EventViewSet, basename = "event")
router.register(r"eventattendances", views.EventAttendanceViewSet, basename = "eventattendance")
router.register(r"invitation", views.InvitationViewSet, basename = "invitation")

router.register(r"videos", views.InstructionalVideoViewSet, basename = "video")
router.register(r"adaptations", views.AdaptationStoryViewSet, basename = "adaptation")
router.register(r"documentations", views.DocumentationViewSet, basename = "documentation")

router.register(r"projects", views.ProjectViewSet, basename = "project")
router.register(r"projectuserss", views.ProjectUserViewSet, basename = "projectuser")
router.register(r"plans", views.PlanViewSet, basename = "plan")
router.register(r"feedbacks", views.FeedbackViewSet, basename = "feedback")

router.register(r"actions", views.ActionViewSet, basename = "action")
router.register(r"questions", views.QuestionViewSet, basename = "question")
router.register(r"goals", views.GoalViewSet, basename = "goal")
router.register(r"actors", views.ActorViewSet, basename = "actor")

router.register(r"projectgoals", views.ProjectGoalViewSet, basename = "projectgoal")
router.register(r"projectactors", views.ProjectActorViewSet, basename = "projectactor")
router.register(r"projectactions", views.ProjectActionViewSet, basename = "projectaction")
router.register(r"projectquestions", views.ProjectQuestionViewSet, basename = "projectquestion")
router.register(r"projectplans", views.ProjectPlanViewSet, basename = "projectplan")

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path("", TemplateView.as_view(template_name="interactwel/application.html"), name="app")
]
