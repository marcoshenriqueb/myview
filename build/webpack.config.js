var path = require('path');
var webpack = require('webpack');
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var OptimizeCSSPlugin = require('optimize-css-assets-webpack-plugin');
var BabiliPlugin = require("babili-webpack-plugin");

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = function(env) {
  if (env === 'production') {
    var plugins = [
      new webpack.DefinePlugin({
        'process.env': require('./../env').prod
      }),
      new ExtractTextPlugin('css/[name].css'),
      new BabiliPlugin({
        sourceMap: true
      }),
      // Compress extracted CSS. We are using this plugin so that possible
      // duplicated CSS from different components can be deduped.
      new OptimizeCSSPlugin({
        cssProcessorOptions: {
          safe: true
        }
      })
    ];
  } else {
    var plugins = [
      new webpack.DefinePlugin({
        'process.env': require('./../env').dev
      }),
      new ExtractTextPlugin('css/[name].css'),
      new webpack.NoEmitOnErrorsPlugin(),
      // https://github.com/ampedandwired/html-webpack-plugin
      new FriendlyErrorsPlugin()
    ];
  }
  return {
    entry: {
      home: resolve('home/static/home/js/home.js')
    },
    devtool: env !== 'production' ? '#cheap-module-eval-source-map' : '#source-map',
    output: {
      path: resolve('static'),
      publicPath: '/static/',
      filename: '[name].js'
    },
    watch: env !== 'production' ? true : false,
    module: {
    rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
          include: [resolve('src')]
        },
        {
          test: /\.(css|styl)$/,
          use: ExtractTextPlugin.extract({
            fallback: 'style-loader',
            //resolve-url-loader may be chained before sass-loader if necessary
            use: [
              'css-loader',
              {
                loader: 'postcss-loader',
                options: {
                  sourceMap: true,
                  plugins: () => [ 
                    require('autoprefixer') 
                  ]
                }
              },
              'stylus-loader'
            ]
          })
        }
      ]
    },
    plugins: plugins
  };
};