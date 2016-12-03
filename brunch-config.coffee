exports.config =
  npm:
    enabled: true
    globals:
      $: 'jquery'
      jQuery: 'jquery'
    whitelist: ["jquery", "bootstrap-sass"]
  plugins:
    babel:
      presets: ['es2015', 'es2016', 'react', 'stage-0']
      pattern: /\.(js|es6|jsx)$/
    sass:
      options:
        includePaths: ["node_modules/bootstrap-sass/assets/stylesheets"]
        precision: 8
    copycat:
      "fonts": ["node_modules/bootstrap-sass/assets/fonts/bootstrap"]
    eslint:
      pattern: /^ui\/.*\.js?x?$/
      warnOnly: false
  paths:
    public: 'rippl/questing/static/'
    watched: ['ui']
  files:
    javascripts:
      joinTo:
        'vendor.js': /^node_modules/
        'app.js': /^ui/
    stylesheets:
      joinTo:
        'app.css': /^ui/

  overrides:
    production:
      optimize: true
      sourceMaps: false
