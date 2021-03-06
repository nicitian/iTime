const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const merge = require('webpack-merge');
const webpackBaseConfig = require('./webpack.base.config.js');
const fs = require('fs');
const CleanWebpackPlugin = require("clean-webpack-plugin");
fs.open('./src/config/env.js', 'w', function (err, fd) {
    const buf = 'export default "production";';
    fs.write(fd, buf, 0, buf.length, 0, function (err, written, buffer){});
});

module.exports = merge(webpackBaseConfig, {
    output: {
        publicPath: '',
        filename: '[name].[hash:8].js',
        chunkFilename: '[name].[hash:8].chunk.js'
    },
    devtool:'null',
    plugins: [
        new ExtractTextPlugin({
            filename: '[name].[hash:8].css',
            allChunks: true
        }),
         new webpack.optimize.CommonsChunkPlugin({
            name: 'vendors',
            filename: 'vendors.[hash:8].js'
        }),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            }
        }),
        new HtmlWebpackPlugin({
            // filename: '../../../login/templates/register_.html',
            // template: './src/template/regist.ejs',
            // filename: '../../../login/templates/login/login_.html',
            // template: './src/template/login.ejs',
            filename: '../../login/templates/index_.html',
            template: './src/template/index_prod.ejs',
            inject: false
        }),
        new CleanWebpackPlugin('dist/*.*', {
            // new CleanWebpackPlugin('dist/login/*.*', {
        // new CleanWebpackPlugin('dist/regist/*.*', {
            root: __dirname,
            verbose: true,
            dry: false
        })
    ]
});