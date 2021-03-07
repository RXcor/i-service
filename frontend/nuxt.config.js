const pkg = require('./package')
const webpack = require("webpack")


module.exports = {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    "~/assets/css/bootstrap.min.css",
    "~/assets/font-awesome/css/font-awesome.css",
    "~/assets/css/animate.css",
    "~/assets/css/style.css"
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    "~/plugins/bootstrap.js",
    "~/plugins/metismenu.js",
    "~/plugins/slimscroll.js",
    "~/plugins/inspinia.js"
  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
  ],

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    plugins:[
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery:"jquery"
      })
    ],
    extend(config, ctx) {
      
    }
  }
}
