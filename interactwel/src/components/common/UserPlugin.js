export default {
    install(Vue, options) {

        Vue.mixin({
            data() {
                return {
                    projectsUsers:[]
                };
            },

            methods: {
                async getLoggedInUser() {
                    const { utils } = AiravataAPI;
                    const SessionData = AiravataPortalSessionData;
                    const username = SessionData.username;
                    return await utils.FetchUtils.get("/interactwel/api/users/")
                        .then(users => {
                            return users.find(user => {
                                return user.username === username;
                            });
                        })
                        .catch(error => {
                            alert("API error! while getting the logged in user information" + error);
                        });
                },

                async getProjectsListOfLoggedInUser() {
                    let user = await this.getLoggedInUser();
                    const { utils } = AiravataAPI;
                    this.projectsUsers = await utils.FetchUtils.get("/interactwel/api/projectusers/")
                        .then(users => {
                            return  users.filter(projectUser => {
                                return projectUser.user_id === user.id;
                            })
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });

                    return  await utils.FetchUtils.get("/interactwel/api/projects/")
                        .then(projects => {
                            return projects.filter(project => {
                                return this.projectsUsers.findIndex(projectUser => {
                                    return projectUser.project_id === project.project_id;
                                }) !== -1 ? true : false;
                            });
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });

                },

                async getProjectsListWithPlansOfLoggedInUser() {
                    let user = await this.getLoggedInUser();
                    const { utils } = AiravataAPI;
                    this.projectsUsers = await utils.FetchUtils.get("/interactwel/api/projectusers/")
                        .then(users => {
                            return  users.filter(projectUser => {
                                return projectUser.user_id === user.id && projectUser.status === "Active";
                            })
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });

                    return  await utils.FetchUtils.get("/interactwel/api/projects/")
                        .then(projects => {
                            projects = projects.filter(project => {
                                return this.projectsUsers.findIndex(projectUser => {
                                    return projectUser.project_id === project.project_id;
                                }) !== -1 ? true : false;
                            });
                            return projects;
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });

                },

                async getPlans(projectId) {
                    const {utils} = AiravataAPI;
                    return await utils.FetchUtils.get("/interactwel/api/plans/?project_id=" + projectId)
                        .then(projectPlansList => {
                            return  projectPlansList;
                        })
                        .catch(error => {
                            alert("Could not get the plans list. API error! " + error);
                        });
                },

                async getPlanById(planId) {
                    const {utils} = AiravataAPI;
                    return await utils.FetchUtils.get("/interactwel/api/plans/?plan_id=" + planId)
                        .then(projectPlansList => {
                            return  projectPlansList;
                        })
                        .catch(error => {
                            alert("Could not get the plans list. API error! " + error);
                        });
                },

                async getProjectPlans(projectId) {
                    const {utils} = AiravataAPI;
                    return await utils.FetchUtils.get("/interactwel/api/plans/?project_id=" + projectId)
                        .then(projectPlansList => {
                            return  projectPlansList;
                        })
                        .catch(error => {
                            alert("Could not get the plans list. API error! " + error);
                        });
                },

                async getProjectGoals(projectId) {
                    const {utils} = AiravataAPI;
                    this.projectsGoals = await utils.FetchUtils.get("/interactwel/api/projectgoals/")
                        .then(projectsGoals => {
                            return  projectsGoals.filter(projectgoal => {
                                return projectgoal.project_id == projectId;
                            })
                        })
                        .catch(error => {
                            alert("Could not get the goal list. API error! " + error);
                        });

                    return  await utils.FetchUtils.get("/interactwel/api/goals/")
                        .then(goals => {
                            return goals.filter(goal => {
                                return this.projectsGoals.findIndex(projectsGoal => {
                                    return projectsGoal.goal_id === goal.goal_id;
                                }) !== -1 ? true : false;
                            });
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });
                },

                async getProjectActors(projectId) {
                    const {utils} = AiravataAPI;
                    this.projectActors = await utils.FetchUtils.get("/interactwel/api/projectactors/")
                        .then(projectActors => {
                            return  projectActors.filter(projectActor => {
                                return projectActor.project_id == projectId;
                            })
                        })
                        .catch(error => {
                            alert("Could not get the goal list. API error! " + error);
                        });

                    return  await utils.FetchUtils.get("/interactwel/api/actors/")
                        .then(actors => {
                            return actors.filter(actor => {
                                return this.projectActors.findIndex(projectActor => {
                                    return projectActor.actor_id === actor.actor_id;
                                }) !== -1 ? true : false;
                            });
                        })
                        .catch(error => {
                            alert("Could not get the projects list. API error! " + error);
                        });
                },

                async getActorActions(planId, actorId) {
                    const {utils} = AiravataAPI;
                    this.planActorActions = await utils.FetchUtils.get("/interactwel/api/planactoraction/?plan_id=" + planId + "&actor_id=" + actorId)
                        .then(planActorActions => {
                            return  planActorActions.filter(planActorAction => {
                                return planActorAction.plan_id == planId && planActorAction.actor_id == actorId;
                            })
                        })
                        .catch(error => {
                            alert("Could not get the planActorActions list. API error! " + error);
                        });

                    return  await utils.FetchUtils.get("/interactwel/api/actions/")
                        .then(actions => {
                            return actions.filter(action => {
                                return this.planActorActions.findIndex(planActorAction => {
                                    return planActorAction.action_id === action.action_id;
                                }) !== -1 ? true : false;
                            });
                        })
                        .catch(error => {
                            alert("Could not get the action list. API error! " + error);
                        });
                },

                async getUserRoles() {
                    const { utils } = AiravataAPI;
                    const user = await this.getLoggedInUser();
                    let roles = await utils.FetchUtils.get("/interactwel/api/roles/")
                        .then(roleSet => {
                            return  roleSet;
                        })
                        .catch(error => {
                            alert("Could not get the user roles list. API error! " + error);
                        });
                    const userRoles = await utils.FetchUtils.get("/interactwel/api/userroles/")
                        .then(userRoles =>
                          userRoles.filter(role=>role.user_id === user.id) //todo - this filtering should happen in backend
                            .map(userRole => roles.find(role => role.role_id === userRole.role_id)))
                        .catch(error => {
                            alert("Could not get the user roles list. API error! " + error);
                        });

                    return userRoles || [];
                }
            }
        })
    }
}