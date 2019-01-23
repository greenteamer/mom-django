var path = require('path')
var webpack = require('webpack')

module.exports = {
  devtool: 'eval',
  mode: 'development',
  entry: [
    './src/index'
  ],
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  resolve: {
    extensions: ['.js', '.jsx', '.mjs']
  },
  module: {
    rules: [
      {
        loader: 'babel-loader',
      },
      // {
      //   test: /\.js$/,
      //   exclude: /node_modules/,
      //   use: ['babel-loader', 'eslint-loader']
      // },
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: 'javascript/auto'
      },
    ]
  }
}
