from rest_framework import viewsets

from .models import Subbasin, InteractwelUser, InteractwelRole, InteractwelInstructionalVideo, \
InteractwelAdaptationStory, InteractwelDocumentation, InteractwelGroup, InteractwelGroupRoleMapping, \
InteractwelGroupMembership, InteractwelEvent, InteractwelEventAttendance, InteractwelInvitation, \
InteractwelProject, InteractwelProjectUser, InteractwelProjectData, InteractwelPlan, InteractwelFeedback, InteractwelGoal, \
InteractwelActor, InteractwelAction, InteractwelQuestion, InteractwelProjectGoal, InteractwelProjectActor, \
InteractwelProjectAction, InteractwelProjectQuestion, InteractwelProjectPlan

from .serializers import SubbasinSerializer, InteractwelUserSerializer, InteractwelRoleSerializer, \
InteractwelInstructionalVideoSerializer, InteractwelAdaptationStorySerializer, \
InteractwelDocumentationSerializer, InteractwelGroupSerializer, InteractwelGroupRoleMappingSerializer, \
InteractwelGroupMembershipSerializer, InteractwelEventSerializer, InteractwelEventAttendanceSerializer, \
InteractwelInvitationSerializer, InteractwelProjectSerializer, InteractwelProjectUserSerializer, InteractwelProjectDataSerializer, \
InteractwelPlanSerializer, InteractwelFeedbackSerializer, InteractwelGoalSerializer, InteractwelActorSerializer, \
InteractwelActionSerializer, InteractwelQuestionSerializer, InteractwelProjectGoalSerializer, InteractwelProjectActorSerializer, \
InteractwelProjectActionSerializer, InteractwelProjectQuestionSerializer, InteractwelProjectPlanSerializer, InteractwelFeedbackAnswerSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics

class SubbasinViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Subbasin.objects.all()
        serializer = SubbasinSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Subbasin.objects.all()
        subbasin = get_object_or_404(queryset, pk=pk)
        serializer = SubbasinSerializer(subbasin)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubbasinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subbasin Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

################# User Management ##############################################
################################################################################

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelUser.objects.all()
        serializer = InteractwelUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelUser.objects.all()
        interactwel_user = get_object_or_404(queryset, username=pk)
        serializer = InteractwelUserSerializer(interactwel_user)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "User Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class RoleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelRole.objects.all()
        serializer = InteractwelRoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelRole.objects.all()
        roles = queryset.filter(role_id=pk)
        serializer = InteractwelRoleSerializer(roles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "User Role Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class GroupViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelGroup.objects.all()
        serializer = InteractwelGroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelGroup.objects.all()
        group = get_object_or_404(queryset, group_id=pk)
        serializer = InteractwelGroupSerializer(group)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "User Group Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class GroupRoleMappingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelGroupRoleMapping.objects.all()
        serializer = InteractwelGroupRoleMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelGroupRoleMapping.objects.all()
        groups = queryset.filter(group_id=pk)
        serializer = InteractwelGroupRoleMappingSerializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelGroupRoleMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Group Role Mapping Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class GroupMembershipViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelGroupMembership.objects.all()
        serializer = InteractwelGroupMembershipSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelGroupMembership.objects.all()
        groups = queryset.filter(group_id=pk)
        serializer = InteractwelGroupMembershipSerializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelGroupMembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Group Membership Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)


################################## Events ######################################
################################################################################

class EventViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelEvent.objects.all()
        serializer = InteractwelEventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelEvent.objects.all()
        event = get_object_or_404(queryset, event_id=pk)
        serializer = InteractwelEventSerializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Event Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class EventAttendanceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelEventAttendance.objects.all()
        serializer = InteractwelEventAttendanceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelEventAttendance.objects.all()
        groups = queryset.filter(event_id=pk)
        serializer = InteractwelEventAttendanceSerializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelEventAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Event Attendance Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class InvitationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelInvitation.objects.all()
        serializer = InteractwelInvitationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelInvitation.objects.all()
        groups = queryset.filter(event_id=pk)
        serializer = InteractwelInvitationSerializer(groups, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelInvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Event Invitation Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

################################################################################
################################################################################

class InstructionalVideoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelInstructionalVideo.objects.all()
        serializer = InteractwelInstructionalVideoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelInstructionalVideo.objects.all()
        interactwel_video = get_object_or_404(queryset, video_id=pk)
        serializer = InteractwelInstructionalVideoSerializer(interactwel_video)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelInstructionalVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Intruction Video Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class AdaptationStoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelAdaptationStory.objects.all()
        serializer = InteractwelAdaptationStorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelAdaptationStory.objects.all()
        interactwel_adaptation = get_object_or_404(queryset, story_id=pk)
        serializer = InteractwelAdaptationStorySerializer(interactwel_adaptation)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelAdaptationStorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Adaptation Story Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class DocumentationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelDocumentation.objects.all()
        serializer = InteractwelDocumentationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelDocumentation.objects.all()
        doc = get_object_or_404(queryset, story_id=pk)
        serializer = InteractwelDocumentationSerializer(doc)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelDocumentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Documentation Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

########################### Project ############################################
################################################################################

class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProject.objects.all()
        serializer = InteractwelProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProject.objects.all()
        project = get_object_or_404(queryset, project_id=pk)
        serializer = InteractwelProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ProjectUserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectUser.objects.all()
        serializer = InteractwelProjectUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectUser.objects.all()
        users = queryset.filter(user_id=pk)
        serializer = InteractwelProjectUserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project User Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ProjectDataViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectData.objects.all()
        serializer = InteractwelProjectDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectData.objects.all()
        data = queryset.filter(name=pk)
        serializer = InteractwelProjectDataSerializer(data, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Data Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class PlanViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelPlan.objects.all()
        serializer = InteractwelPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelPlan.objects.all()
        project = get_object_or_404(queryset, plan_id=pk)
        serializer = InteractwelPlanSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Plan Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class FeedbackViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InteractwelFeedbackSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelFeedback.objects.all()
        feedbacks = queryset.filter(user_id=pk)
        serializer = InteractwelFeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Feedback Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)
    
    def get_queryset(self):
        queryset = InteractwelFeedback.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        plan_id = self.request.query_params.get('plan_id', None)
        if plan_id is not None:
            queryset = queryset.filter(plan_id=plan_id)

        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)

        return queryset

class FeedbackAnswerViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = InteractwelFeedbackAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Feedback Answer Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)


########################### Goals Actors Actions Questions #####################
################################################################################

class GoalViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelGoal.objects.all()
        serializer = InteractwelGoalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelGoal.objects.all()
        goal = get_object_or_404(queryset, goal_id=pk)
        serializer = InteractwelGoalSerializer(goal)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Goal Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ActorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelActor.objects.all()
        serializer = InteractwelActorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelActor.objects.all()
        actor = get_object_or_404(queryset, actor_id=pk)
        serializer = InteractwelActorSerializer(actor)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Actor Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ActionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelAction.objects.all()
        serializer = InteractwelActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelAction.objects.all()
        action = get_object_or_404(queryset, action_id=pk)
        serializer = InteractwelActionSerializer(action)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Action Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class QuestionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelQuestion.objects.all()
        serializer = InteractwelQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelQuestion.objects.all()
        project = get_object_or_404(queryset, question_id=pk)
        serializer = InteractwelQuestionSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Question Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

########################### Project mapping in Goals Actors Actions Questions ##
################################################################################

class ProjectGoalViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectGoal.objects.all()
        serializer = InteractwelProjectGoalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectGoal.objects.all()
        goals = queryset.filter(project_id=pk)
        serializer = InteractwelProjectGoalSerializer(goals, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Goal Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ProjectActorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectActor.objects.all()
        serializer = InteractwelProjectActorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectActor.objects.all()
        actors = queryset.filter(project_id=pk)
        serializer = InteractwelProjectActorSerializer(actors, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Actor Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ProjectActionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectAction.objects.all()
        serializer = InteractwelProjectActionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectAction.objects.all()
        actors = queryset.filter(project_id=pk)
        serializer = InteractwelProjectActionSerializer(actors, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Action Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class ProjectQuestionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InteractwelProjectQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectQuestion.objects.all()
        questions = queryset.filter(project_id=pk)
        serializer = InteractwelProjectQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Question Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

    def get_queryset(self):
        queryset = InteractwelProjectQuestion.objects.all()
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)

        question_id = self.request.query_params.get('question_id', None)
        if question_id is not None:
            queryset = queryset.filter(question_id=question_id)
        return queryset

class ProjectPlanViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelProjectPlan.objects.all()
        serializer = InteractwelProjectPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelProjectPlan.objects.all()
        plans = queryset.filter(project_id=pk)
        serializer = InteractwelProjectPlanSerializer(plans, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelProjectPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message", "Project Plan Created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)