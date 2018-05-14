const ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  devtool:'eval-source-map',
  entry:__dirname + "/app/main.js",//已多次提及的唯一入口文件
  output:{
    path:__dirname + "/dist",//打包后的文件存放的地方
    filename: "main.js"//打包后输出文件的文件名
  },
  devServer:{
  	contentBase:"./public",
  	historyApiFallback:true,
  	inline:true
  },
  module:{
  	rules:[
    {
      test:/\.vue$/,
      loader:'vue-loader',
      options:{
        loaders:{
          css:ExtractTextPlugin.extract({
            use:'css-loader',
            fallback:'style-loader'
          })
        }
      }
    },
  		{
  			test:/(\.jsx|\.js)$/,
  			use:{
  				loader:"babel-loader",
  			},
  			exclude:/node_modules/
  		},
  		{
  			test:/\.css$/,
  			use:ExtractTextPlugin.extract({
          use:'css-loader',
          fallback:'style-loader'
        })
  		},
  		{
  			test:/\.vue$/,
        loader:'vue-loader',
  			options:{
          loaders:{
            css:ExtractTextPlugin.extract({
              use:'css-loader',
              fallback:'style-loader'
            })
          }
        }
  		}
  	]
  },
  plugins:[
    new ExtractTextPlugin('main.css')
  ]
}
  