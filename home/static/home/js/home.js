import 'normalize.css';
import './../css/paraxify.css';
import './../styl/home.styl';

import './../js/paraxify';
import Shuffle from 'shufflejs';
import Vimeo from '@vimeo/player';

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mobile-menu').addEventListener('click', () => {
        document.querySelector('header.header').classList.toggle('active');
    });

    // Adjusts cover video size
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

    // Parallax home page
    paraxify('.paraxify');

    // Adjusts home page projects container size
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

    // Vimeo lightbox
    document.querySelectorAll('.start-video').forEach((d) => {
        d.addEventListener('click', (e) => {
            e.preventDefault();
            const overlay = document.createElement('div');
            overlay.id = 'body-overlay';
            overlay.classList.add('body-overlay');
            document.body.appendChild(overlay);
            const close = document.createElement('span');
            close.classList.add('fa');
            close.classList.add('fa-close');
            close.addEventListener('click', () => {
                overlay.parentNode.removeChild(overlay);
            });
            overlay.addEventListener('click', (e) => {
                if (e.target.id === 'body-overlay') {
                    overlay.parentNode.removeChild(overlay);
                }
            });
            overlay.appendChild(close);
            const video = document.createElement('div');
            video.classList.add('video-player');
            overlay.appendChild(video);
            const width = (overlay.offsetWidth * 0.8).toFixed(0);
            const player = new Vimeo(video, {
                id: e.target.dataset.id,
                width
            });
        });
    });

    // Shuffle for projects page
    const grid = document.getElementById('grid');
    if (grid) {
        const shuffle = new Shuffle(grid, {
          itemSelector: '.projects-content_item',
          gutterWidth: 20,
          columnWidth: (w) => {
            let width = (w / 3) - 15;
            if (w < 400) {
                width = w;
            } else if (w < 750) {
                width = (w / 2) - 10;
            }
            document.querySelectorAll('.projects-content_item').forEach((item) => {
                item.style.width = width + 'px';
                item.style.height = width + 'px';
            });
            return width;
          },
        });
        document.querySelectorAll('.project-filter-button').forEach((button) => {
            button.addEventListener('click', (e) => {
                e.target.classList.toggle('active');
                shuffle.filter(e.target.id);
            })
        });
    }

    const onResize = () => {
        adjustProjectContainers();
        if (v) {
            adjustVideo();
        }
    };
    window.onresize = onResize;
});
