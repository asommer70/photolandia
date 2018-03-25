const fs = require('fs');
const https = require('https');

const assets =  './assets/js/vendor/';
const cssAssets =  './assets/css/vendor/';

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
