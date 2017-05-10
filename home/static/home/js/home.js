import 'normalize.css';
import './../styl/home.styl';

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mobile-menu').addEventListener('click', () => {
        document.querySelector('header.header').classList.toggle('active');
    });


    const adjustVideo = () => {
        const w = window.innerWidth;
        if (w > 768) {
            const vRatio = v.videoHeight / v.videoWidth;
            top.style.height = (vRatio * w) + 'px';
        } else {
            top.style.height = 'calc(100vh - 100px)';
        }
    }
    const top = document.querySelector('.top');
    const v = document.getElementsByTagName('video')[0];
    v.addEventListener('loadeddata', () => {
        adjustVideo();
    });
    window.onresize = adjustVideo;
});
