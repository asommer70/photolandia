const fs = require('fs');
const https = require('https');
const ncp = require('ncp').ncp;

ncp.limit = 16;

const assets =  '../assets/js/vendor/';
const cssAssets =  '../assets/css/vendor/';

if (!fs.existsSync(assets)){
    fs.mkdirSync(assets);
}

if (!fs.existsSync(cssAssets)){
    fs.mkdirSync(cssAssets);
}

fs.createReadStream('./node_modules/foundation-sites/dist/js/foundation.min.js')
  .pipe(fs.createWriteStream(assets + 'foundation.min.js'));

fs.createReadStream('./node_modules/jquery/dist/jquery.min.js')
  .pipe(fs.createWriteStream(assets + 'jquery.min.js'));

  fs.createReadStream('./node_modules/mousetrap/mousetrap.min.js')
    .pipe(fs.createWriteStream(assets + 'mousetrap.min.js'));

fs.createReadStream('./node_modules/photoswipe/dist/photoswipe.min.js')
  .pipe(fs.createWriteStream(assets + 'photoswipe.min.js'));

fs.createReadStream('./node_modules/photoswipe/dist/photoswipe-ui-default.min.js')
  .pipe(fs.createWriteStream(assets + 'photoswipe-ui-default.min.js'));

fs.createReadStream('./node_modules/photoswipe/dist/photoswipe.css')
  .pipe(fs.createWriteStream(cssAssets + 'photoswipe.css'));

  if (!fs.existsSync(cssAssets + '/default-skin')){
      fs.mkdirSync(cssAssets + '/default-skin');
  }
ncp('./node_modules/photoswipe/dist/default-skin/', cssAssets + '/default-skin', function (err) {
 if (err) {
   console.error('ncp photoswipe/dist/default-skin err:', err);
 }
});
