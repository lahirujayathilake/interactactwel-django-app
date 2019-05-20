module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/interactactwel-django-app/'
        : '/'
}