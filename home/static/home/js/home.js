import 'normalize.css';
import './../styl/home.styl';

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('mobile-menu').addEventListener('click', () => {
        document.querySelector('header.header').classList.toggle('active');
    });
});
