from rest_framework import serializers
from django.db import models
from jsonfield import JSONField

class Subbasin(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    detail_json = JSONField()

    class Meta:
        managed = True
        db_table = 'subbasin'
        verbose_name = 'Subbasin'
        verbose_name_plural = 'Subbasins'

################# User Management ##############################################
################################################################################

class InteractwelUser(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    organization = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'interactwel_user'
        verbose_name = 'Interactwel User'
        verbose_name_plural = 'Interactwel Users'
        unique_together = (('username',),)

class InteractwelRole(models.Model):
    role_id = models.BigAutoField(primary_key=True, editable=False)
    role_name = models.CharField(max_length=64)
    role_description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_role'
        verbose_name = 'Interactwel Role'
        verbose_name_plural = 'Interactwel Role'
        unique_together = (('role_name'),)

class InteractwelGroup(models.Model):
    group_id = models.BigAutoField(primary_key=True, editable=False)
    group_name = models.CharField(max_length=64)
    group_description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_group'
        verbose_name = 'Interactwel Group'
        verbose_name_plural = 'Interactwel Group'
        unique_together = (('group_name'),)

class InteractwelGroupRoleMapping(models.Model):
    group_id = models.ForeignKey(InteractwelGroup, on_delete=models.CASCADE)
    role_id = models.ForeignKey(InteractwelRole, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_group_role_mapping'
        verbose_name = 'Interactwel Group Role Mapping'
        verbose_name_plural = 'Interactwel Group Role Mapping'
        unique_together = (('group_id', 'role_id'),)

class InteractwelGroupMembership(models.Model):
    group_id = models.ForeignKey(InteractwelGroup, on_delete=models.CASCADE)
    user_id = models.ForeignKey(InteractwelUser, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_group_membership'
        verbose_name = 'Interactwel Group Membership'
        verbose_name_plural = 'Interactwel Group Membership'
        unique_together = (('group_id', 'user_id'),)

################################## Events ######################################
################################################################################

class InteractwelEvent(models.Model):
    event_id = models.BigAutoField(primary_key=True, editable=False)
    event_name = models.CharField(max_length=256)
    event_description = models.CharField(max_length=256)
    event_date = models.fields.DateTimeField()
    even_location = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_event'
        verbose_name = 'Interactwel Event'
        verbose_name_plural = 'Interactwel Event'

class InteractwelEventAttendance(models.Model):
    event_id = models.ForeignKey(InteractwelEvent, on_delete=models.CASCADE)
    user_id = models.ForeignKey(InteractwelUser, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_event_attendence'
        verbose_name = 'Interactwel Event Attendence'
        verbose_name_plural = 'Interactwel Event Attendance'
        unique_together = (('event_id', 'user_id'),)

class InteractwelInvitation(models.Model):
    inviter_id = models.ForeignKey(InteractwelUser, related_name='inviter_id', on_delete=models.CASCADE)
    invitee_id = models.ForeignKey(InteractwelUser, related_name='invitee_id', on_delete=models.CASCADE)
    event_id = models.ForeignKey(InteractwelEvent, on_delete=models.CASCADE)
    invite_status = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_invitation'
        verbose_name = 'Interactwel Invitation'
        verbose_name_plural = 'Interactwel Invitation'
        unique_together = (('event_id', 'inviter_id', 'invitee_id'),)



################################################################################
################################################################################

class InteractwelInstructionalVideo(models.Model):
    video_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_vidos'
        verbose_name = 'Interactwel Videos'
        verbose_name_plural = 'Interactwel Videos'

class InteractwelAdaptationStory(models.Model):
    story_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_sdaptation_story'
        verbose_name = 'Interactwel Adaptation Stories'
        verbose_name_plural = 'Interactwel Adaptation Stories'


class InteractwelDocumentation(models.Model):
    doc_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    data = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_documentation'
        verbose_name = 'Interactwel Documentation'
        verbose_name_plural = 'Interactwel Documentation'

########################### Goals Actors Actions Questions #####################
################################################################################

class InteractwelGoal(models.Model):
    goal_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_goal'
        verbose_name = 'Interactwel Goal'
        verbose_name_plural = 'Interactwel Goal'

class InteractwelActor(models.Model):
    actor_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_actor'
        verbose_name = 'Interactwel Actor'
        verbose_name_plural = 'Interactwel Actor'

class InteractwelAction(models.Model):
    action_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_action'
        verbose_name = 'Interactwel Action'
        verbose_name_plural = 'Interactwel Action'

class InteractwelQuestion(models.Model):
    question_id = models.BigAutoField(primary_key=True, editable=False)
    label = models.CharField(max_length=256)
    question_type = models.CharField(max_length=256)
    question_text = models.CharField(max_length=1024)
    possible_answers = models.CharField(max_length=1024)

    class Meta:
        managed = True
        db_table = 'interactwel_question'
        verbose_name = 'Interactwel Question'
        verbose_name_plural = 'Interactwel Question'

########################### Project ############################################
################################################################################

class InteractwelProject(models.Model):
    project_id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    latitude = models.CharField(max_length=256)
    longtitude = models.CharField(max_length=256)
    feedbackProvided = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'interactwel_project'
        verbose_name = 'Interactwel Project'
        verbose_name_plural = 'Interactwel Project'

class InteractwelProjectUser(models.Model):
    user_id = models.ForeignKey(InteractwelUser, on_delete=models.CASCADE)
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)

    status = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    sector = models.CharField(max_length=256)
    actor = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'interactwel_project_user'
        verbose_name = 'Interactwel Project User'
        verbose_name_plural = 'Interactwel Project User'
        unique_together = (('user_id', 'project_id'),)

class InteractwelPlan(models.Model):
    plan_id = models.BigAutoField(primary_key=True, editable=False)
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    user_id = models.ForeignKey(InteractwelUser, on_delete=models.CASCADE)
    goals = models.ManyToManyField('InteractwelGoal', related_name='plans', blank=True)
    actors = models.ManyToManyField('InteractwelActor', related_name='actors', blank=True)
    actions = models.ManyToManyField('InteractwelAction', related_name='actions', blank=True)
    timestamp = models.fields.DateTimeField()

    class Meta:
        managed = True
        db_table = 'interactwel_plan'
        verbose_name = 'Interactwel Plan'
        verbose_name_plural = 'Interactwel Plan'

class InteractwelFeedback(models.Model):
    feedback_id = models.BigAutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(InteractwelUser, on_delete=models.CASCADE)
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(InteractwelPlan, on_delete=models.CASCADE)

    date_created = models.fields.DateTimeField()
    date_modified = models.fields.DateTimeField()
    feasibilty = models.CharField(max_length=256)
    comments = models.CharField(max_length=256, null = True)
    rating = models.CharField(max_length=256, null = True)

    class Meta:
        managed = True
        db_table = 'interactwel_feedback'
        verbose_name = 'Interactwel Feedback'
        verbose_name_plural = 'Interactwel Feedback'
        unique_together = (('user_id', 'project_id', 'plan_id'),)

class InteractwelFeedbackAnswer(models.Model):
    feedback_id = models.ForeignKey(InteractwelFeedback, related_name='feedback_answers', on_delete=models.CASCADE)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)

    class Meta:
        managed = True
        db_table = 'interactwel_feedback_answer'
        verbose_name = 'Interactwel Feedback Answer'
        verbose_name_plural = 'Interactwel Feedback Answer'

    def __str__(self):
        return '%s' % (self.question)

class InteractwelProjectData(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=256)
    data = models.TextField(blank=True)
    
    class Meta:
        managed = True
        db_table = 'interactwel_project_data'
        verbose_name = 'Interactwel Project Data'
        verbose_name_plural = 'Interactwel Project Data'
        unique_together = (('name', 'project_id'),)
########################### Project mapping in Goals Actors Actions Questions ##
################################################################################

class InteractwelProjectGoal(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    goal_id = models.ForeignKey(InteractwelGoal, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_project_goal'
        verbose_name = 'Interactwel Project Goal'
        verbose_name_plural = 'Interactwel Project Goal'
        unique_together = (('project_id', 'goal_id'),)

class InteractwelProjectActor(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(InteractwelActor, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_project_actor'
        verbose_name = 'Interactwel Project Actor'
        verbose_name_plural = 'Interactwel Project Actor'
        unique_together = (('project_id', 'actor_id'),)

class InteractwelProjectAction(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    action_id = models.ForeignKey(InteractwelAction, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_project_action'
        verbose_name = 'Interactwel Project Action'
        verbose_name_plural = 'Interactwel Project Action'
        unique_together = (('project_id', 'action_id'),)

class InteractwelProjectQuestion(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    question_id = models.ForeignKey(InteractwelQuestion, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_project_question'
        verbose_name = 'Interactwel Project Question'
        verbose_name_plural = 'Interactwel Project Question'
        unique_together = (('project_id', 'question_id'),)

class InteractwelProjectPlan(models.Model):
    project_id = models.ForeignKey(InteractwelProject, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(InteractwelPlan, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'interactwel_project_plan'
        verbose_name = 'Interactwel Project Plan'
        verbose_name_plural = 'Interactwel Project Plan'
        unique_together = (('project_id', 'plan_id'),)
