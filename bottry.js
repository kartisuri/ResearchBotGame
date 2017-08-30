var mitsuku = require('mitsuku-api')();
var body = '';
process.argv.forEach(function (val, index, array) {
  if (index == 2){body = val;}
});
mitsuku.send(body).then(function(result){console.log(result);});