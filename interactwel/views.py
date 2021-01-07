from rest_framework import viewsets

from .models import Subbasin, InteractwelUser, InteractwelRole, InteractwelUserRole, InteractwelInstructionalVideo, \
InteractwelAdaptationStory, InteractwelDocumentation, InteractwelGroup, InteractwelGroupRoleMapping, \
InteractwelGroupMembership, InteractwelEvent, InteractwelEventAttendance, InteractwelInvitation, \
InteractwelProject, InteractwelProjectUser, InteractwelProjectData, InteractwelPlan, InteractwelFeedback, InteractwelGoal, \
InteractwelActor, InteractwelAction, InteractwelQuestion, InteractwelProjectGoal, InteractwelProjectActor, \
InteractwelProjectAction, InteractwelProjectQuestion, InteractwelProjectPlan, InteractwelPlanActorActions

from .serializers import SubbasinSerializer, InteractwelUserSerializer, InteractwelRoleSerializer, InteractwelUserRoleSerializer, \
InteractwelInstructionalVideoSerializer, InteractwelAdaptationStorySerializer, \
InteractwelDocumentationSerializer, InteractwelGroupSerializer, InteractwelGroupRoleMappingSerializer, \
InteractwelGroupMembershipSerializer, InteractwelEventSerializer, InteractwelEventAttendanceSerializer, \
InteractwelInvitationSerializer, InteractwelProjectSerializer, InteractwelProjectUserSerializer, InteractwelProjectDataSerializer, \
InteractwelPlanSerializer, InteractwelFeedbackSerializer, InteractwelGoalSerializer, InteractwelActorSerializer, \
InteractwelActionSerializer, InteractwelQuestionSerializer, InteractwelProjectGoalSerializer, InteractwelProjectActorSerializer, \
InteractwelProjectActionSerializer, InteractwelProjectQuestionSerializer, InteractwelProjectPlanSerializer, InteractwelFeedbackAnswerSerializer, \
InteractwelPlanActorActionsSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserRoleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InteractwelUserRoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelUserRole.objects.all()
        userroles = queryset.filter(user_id=pk)
        serializer = InteractwelUserRoleSerializer(userroles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelUserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = InteractwelUserRole.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        role_id = self.request.query_params.get('role_id', None)
        if role_id is not None:
            queryset = queryset.filter(role_id=role_id)
        return queryset

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class PlanViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = self.get_queryset()
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = InteractwelPlan.objects.all()
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)

        plan_id = self.request.query_params.get('plan_id', None)
        if plan_id is not None:
            queryset = queryset.filter(plan_id=plan_id)
        return queryset

class PlanActorActionsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InteractwelPlanActorActions.objects.all()
        serializer = InteractwelPlanActorActionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = InteractwelPlanActorActions.objects.all()
        plans = queryset.filter(plan_id=pk)
        serializer = InteractwelPlanActorActionsSerializer(plans, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InteractwelPlanActorActionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            saved = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
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
        serializer = InteractwelFeedbackAnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)