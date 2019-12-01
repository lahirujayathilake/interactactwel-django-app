const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    publicPath:
        process.env.NODE_ENV === "development"
            ? "http://0.0.0.0:9000/static/interactwel/dashboard/dist/": "/static/interactwel/dashboard/dist/",
    // baseUrl: "http://0.0.0.0:8080/",
    outputDir: './static/interactwel/dashboard/dist',

    devServer: {
        disableHostCheck: true
    },

    chainWebpack: config => {

    config.optimization
    .splitChunks(false)

config
    .plugin('BundleTracker')
    .use(BundleTracker, [{filename: './static/interactwel/dashboard/dist/webpack-stats.json'}])

config.resolve.alias
    .set('__STATIC__', 'static')

config.devServer
    .public('http://0.0.0.0:9000')
    .host('0.0.0.0')
    .port(9000)
    .hotOnly(true)
    .watchOptions({poll: 1000})
    .https(false)
    .headers({"Access-Control-Allow-Origin": ["\*"]})
}
};