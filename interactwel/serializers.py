from django.contrib.auth.models import User, Group
from rest_framework import serializers
import json

from .models import Subbasin, InteractwelUser, InteractwelRole, InteractwelUserRole, InteractwelAdaptationStory, \
InteractwelInstructionalVideo, InteractwelDocumentation, InteractwelGroup, \
InteractwelGroupRoleMapping, InteractwelGroupMembership, InteractwelEvent, \
InteractwelEventAttendance, InteractwelInvitation, InteractwelProject, InteractwelProjectUser, \
InteractwelPlan, InteractwelFeedback, InteractwelGoal, InteractwelActor, InteractwelAction, \
InteractwelQuestion, InteractwelProjectGoal, InteractwelProjectActor, InteractwelProjectAction, \
InteractwelProjectQuestion, InteractwelProjectPlan, InteractwelProjectData, InteractwelFeedbackAnswer, \
InteractwelPlanActorActions

class SubbasinSerializer(serializers.ModelSerializer):

    detail_json = serializers.JSONField()
    class Meta:
        model = Subbasin
        fields = ("id", "detail_json")

################# User Management ##############################################
################################################################################

class InteractwelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelUser
        fields = '__all__'

class InteractwelRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelRole
        fields = '__all__'

class InteractwelUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelUserRole
        fields = '__all__'

class InteractwelGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelGroup
        fields = '__all__'

class InteractwelGroupRoleMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelGroupRoleMapping
        fields = '__all__'

class InteractwelGroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelGroupMembership
        fields = '__all__'

################################## Events ######################################
################################################################################

class InteractwelEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelEvent
        fields = '__all__'

class InteractwelEventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelEventAttendance
        fields = '__all__'

class InteractwelInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelInvitation
        fields = '__all__'

################################################################################
################################################################################

class InteractwelInstructionalVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelInstructionalVideo
        fields = '__all__'

class InteractwelAdaptationStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelAdaptationStory
        fields = '__all__'

class InteractwelDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelDocumentation
        fields = '__all__'

########################### Project ############################################
################################################################################

class InteractwelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProject
        fields = '__all__'

class InteractwelProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectUser
        fields = '__all__'

class InteractwelPlanActorActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelPlanActorActions
        fields = '__all__'

class InteractwelPlanSerializer(serializers.ModelSerializer):
    action_mapping = InteractwelPlanActorActionsSerializer(source='interactwelplanactoractions_set', many=True)    
    class Meta:
        model = InteractwelPlan
        fields = ("plan_id", "timestamp", "project_id", "user_id", "goals", "action_mapping")
        extra_kwargs = {'goals': {'required': False}, 'action_mapping': {'required': False}}

class InteractwelFeedbackAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelFeedbackAnswer
        fields = '__all__'

class InteractwelFeedbackSerializer(serializers.ModelSerializer):
    feedback_answers = InteractwelFeedbackAnswerSerializer(many=True, required=False)
    class Meta:
        model = InteractwelFeedback
        fields = '__all__'
        extra_kwargs = {'comments': {'required': False}, 'rating': {'required': False}}

class InteractwelProjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectData
        fields = '__all__'

########################### Goals Actors Actions Questions #####################
################################################################################


class InteractwelGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelGoal
        fields = '__all__'

class InteractwelActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelActor
        fields = '__all__'

class InteractwelActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelAction
        fields = '__all__'

class StoredJSONField(serializers.JSONField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        try:
            if value:
                print(value)
                return json.loads(value)
            else:
                return value
        except Exception:
            return value

    def to_internal_value(self, data):
        try:
            return json.dumps(data)
        except (TypeError, ValueError):
            self.fail('invalid')

class InteractwelQuestionSerializer(serializers.ModelSerializer):

    possible_answers = StoredJSONField()

    class Meta:
        model = InteractwelQuestion
        fields = '__all__'

########################### Project mapping in Goals Actors Actions Questions ##
################################################################################

class InteractwelProjectGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectGoal
        fields = '__all__'

class InteractwelProjectActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectActor
        fields = '__all__'

class InteractwelProjectActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectAction
        fields = '__all__'

class InteractwelProjectQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectQuestion
        fields = '__all__'

class InteractwelProjectPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractwelProjectPlan
        fields = '__all__'