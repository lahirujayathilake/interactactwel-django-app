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
                                return user.username = username;
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
                                return projectUser.user_id === user.id && projectUser.status === "Active";
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

                async getProjectPlans(projectId) {
                    const {utils} = AiravataAPI;
                    return await utils.FetchUtils.get("/interactwel/api/plans/?project_id=" + projectId)
                        .then(projectPlansList => {
                            return  projectPlansList;
                        })
                        .catch(error => {
                            alert("Could not get the plans list. API error! " + error);
                        });
                }
            }
        })
    }
}