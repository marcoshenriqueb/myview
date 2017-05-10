var path = require('path');
var webpack = require('webpack');
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = function(env) {
  if (env === 'production') {
    var plugins = [
      new webpack.DefinePlugin({
        'process.env': require('./../env').prod
      }),
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false
        },
        sourceMap: true
      })
    ];
  } else {
    var plugins = [
      new webpack.DefinePlugin({
        'process.env': require('./../env').dev
      }),
      // https://github.com/glenjamin/webpack-hot-middleware#installation--usage
      new webpack.HotModuleReplacementPlugin(),
      new webpack.NoEmitOnErrorsPlugin(),
      // https://github.com/ampedandwired/html-webpack-plugin
      new FriendlyErrorsPlugin()
    ];
  }
  return {
    entry: {
      app: resolve('home/static/home/js/home.js')
    },
    devtool: env !== 'production' ? '#cheap-module-eval-source-map' : '#source-map',
    output: {
      path: resolve('static'),
      publicPath: '/static/',
      filename: '[name].js'
    },
    module: {
    rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
          include: [resolve('src'), resolve('test')]
        },
        {
          test: /\.styl$/,
          use: [
            'style-loader',
            'css-loader'
          ]
        }
      ]
    },
    plugins: plugins
  };
};