export default {
    install(Vue, options) {

        Vue.mixin({
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
                }
            }
        })
    }
}