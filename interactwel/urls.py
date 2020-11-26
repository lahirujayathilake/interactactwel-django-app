from django.conf.urls import url, include
from django.views.generic import TemplateView

from rest_framework import routers

from . import views

app_name = "interactwel"

router = routers.DefaultRouter()
router.register(r"subbasins", views.SubbasinViewSet, base_name="subbasin")
router.register(r"users", views.UserViewSet, base_name = "user")
router.register(r"roles", views.RoleViewSet, base_name = "role")
router.register(r"userroles", views.UserRoleViewSet, base_name = "userroles")
router.register(r"groups", views.GroupViewSet, base_name = "group")
router.register(r"grouproles", views.GroupRoleMappingViewSet, base_name = "grouprole")
router.register(r"groupmembers", views.GroupMembershipViewSet, base_name = "groupmember")

router.register(r"events", views.EventViewSet, base_name = "event")
router.register(r"eventattendances", views.EventAttendanceViewSet, base_name = "eventattendance")
router.register(r"invitation", views.InvitationViewSet, base_name = "invitation")

router.register(r"videos", views.InstructionalVideoViewSet, base_name = "video")
router.register(r"adaptations", views.AdaptationStoryViewSet, base_name = "adaptation")
router.register(r"documentations", views.DocumentationViewSet, base_name = "documentation")

router.register(r"projects", views.ProjectViewSet, base_name = "project")
router.register(r"projectusers", views.ProjectUserViewSet, base_name = "projectuser")
router.register(r"projectdata", views.ProjectDataViewSet, base_name = "projectdata")
router.register(r"plans", views.PlanViewSet, base_name = "plan")
router.register(r"planactoraction", views.PlanActorActionsViewSet, base_name = "planactoraction")
router.register(r"feedbacks", views.FeedbackViewSet, base_name = "feedback")
router.register(r"feedbackanswers", views.FeedbackAnswerViewSet, base_name = "feedbackanswer")

router.register(r"actions", views.ActionViewSet, base_name = "action")
router.register(r"questions", views.QuestionViewSet, base_name = "question")
router.register(r"goals", views.GoalViewSet, base_name = "goal")
router.register(r"actors", views.ActorViewSet, base_name = "actor")

router.register(r"projectgoals", views.ProjectGoalViewSet, base_name = "projectgoal")
router.register(r"projectactors", views.ProjectActorViewSet, base_name = "projectactor")
router.register(r"projectactions", views.ProjectActionViewSet, base_name = "projectaction")
router.register(r"projectquestions", views.ProjectQuestionViewSet, base_name = "projectquestion")
router.register(r"projectplans", views.ProjectPlanViewSet, base_name = "projectplan")

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(
        "",
        TemplateView.as_view(template_name="interactwel/application.html"),
        name="app",
    )
]
