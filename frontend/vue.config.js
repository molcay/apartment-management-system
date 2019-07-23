const BundleTracker = require("webpack-bundle-tracker")

const _HOST = '0.0.0.0'
const _PORT = 8080
const _URL = `http://${_HOST}:${_PORT}`

module.exports = {
  publicPath: _URL,
  outputDir: './dist/',

  chainWebpack: config => {

    config.optimization.splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .public(_URL)
      .host(_HOST)
      .port(_PORT)
      .hotOnly(true)
      .watchOptions({poll: 1000})
      .https(false)
      .headers({'Access-Control-Allow-Origin': ['\\*']})
  }
}
