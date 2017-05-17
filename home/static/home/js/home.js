import 'normalize.css';
import './../css/paraxify.css';
import './../styl/home.styl';

import './../js/paraxify';

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mobile-menu').addEventListener('click', () => {
        document.querySelector('header.header').classList.toggle('active');
    });


    const adjustVideo = () => {
        const w = window.innerWidth;
        if (w > 768 && top.offsetHeight > v.offsetHeight) {
            const vRatio = (v.videoHeight - 20) / v.videoWidth;
            top.style.height = (vRatio * w) + 'px';
        }
    }

    const top = document.querySelector('.top');
    const v = document.getElementsByTagName('video')[0];
    if (v) {
        v.addEventListener('loadeddata', () => {
            adjustVideo();
        });
    }

    paraxify('.paraxify');

    const adjustProjectContainers = () => {
        const w = window.innerWidth;
        const containers = document.querySelectorAll('.project-container');
        if (w > 868) {
            containers.forEach((c) => {
                c.style.height = (c.querySelector('.project_big img').clientHeight - 2) + 'px';
            });
        } else {
            containers.forEach((c) => {
                c.style.height = null;
            });
        }
    };
    adjustProjectContainers();

    const onResize = () => {
        adjustProjectContainers();
        if (v) {
            adjustVideo();
        }
    };
    window.onresize = onResize;
});
