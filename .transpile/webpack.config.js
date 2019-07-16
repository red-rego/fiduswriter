var webpack = require("webpack");module.exports = {
 mode: "development",
 module: {
  rules: [
   {
    test: /\.(js|mjs)$/,
    exclude: /node_modules/,
    use: {
     loader: "babel-loader",
     options: {
      presets: [
       "@babel/preset-env"
      ],
      plugins: [
       "@babel/plugin-syntax-dynamic-import"
      ]
     }
    }
   }
  ]
 },
 output: {
  path: "/home/rego/Documents/fidus_only/fiduswriter/static-transpile/js/transpile/",
  chunkFilename: "1563278625-[id].js",
  publicPath: "/static/js/transpile/",
 },
 plugins: [
  new webpack.DefinePlugin({   "process.env.TRANSPILE_VERSION": process.env.TRANSPILE_VERSION
  }) ],
 entry: {
  admin_console: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/admin_console.mjs",
  app: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/app.mjs",
  browser_check: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/browser_check.mjs",
  test_caret: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/test_caret.mjs",
  document_template_designer: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/document_template_designer.mjs",
  maintenance: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/maintenance.mjs",
  biblatex_import_worker: "/home/rego/Documents/fidus_only/fiduswriter/.transpile/js/biblatex_import_worker.mjs",
 }
}
