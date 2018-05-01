const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
const webpack = require('webpack')


module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'indexpage use ssr',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'index page use nuxt.js' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  css: [
    // 放这里有点点样式会被覆盖掉，还是在default.vue引入好
    // '~/assets/css/wl.base.css'
  ],
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
      if(!isDev){
        config.plugins.push(new webpack.optimize.ModuleConcatenationPlugin());
        config.plugins.push(new BundleAnalyzerPlugin());
      }
    },
    babel: {
      presets: ['stage-2', 'vue-app']
    },
    vendor: ['axios','element-ui'],
    loaders: [
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        loader: 'url-loader',
        query: {
          limit: 10000, // 10KO
          name: 'img/[name].[hash].[ext]'
        }
      },
      {
        test: /\.css$/,  
        include: [  
          '/assets/css', 
        ],  
        loader: 'style-loader!css-loader'  
      },  
      {
        test: /\.less$/,
        use: [
          'style-loader',
          { loader: 'css-loader', options: { importLoaders: 1 } },
          'less-loader'
        ]
      }
    ]
  },
  plugins: [
    { src: '~/plugins/element-ui', ssr: true },
    { src: '~/plugins/VueLazyload', ssr: false },
    { src: '~/plugins/VueVideoPlayer', ssr: false }
  ]
}
