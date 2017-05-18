const imagemin = require('imagemin');
const imageminJpegtran = require('imagemin-jpegtran');
const imageminPngquant = require('imagemin-pngquant');
var easyimg = require('easyimage');

imagemin(['./build/img/*.{jpg,png}'], './static/img', {
    plugins: [
        imageminJpegtran(),
        imageminPngquant({quality: '65-80'})
    ]
}).then(files => {
    console.log(files);
    files.forEach(function(f) {
        easyimg.resize({
            src: f.path,
            dst: f.path,
            width: 1301,
            ignoreAspectRatio: false
        });
    });
});