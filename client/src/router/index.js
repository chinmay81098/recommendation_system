import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home.vue';
import Recommendation from '../components/Recommendation.vue';

Vue.use(Router);

export default new Router ({
    mode :'history',
    base : 'http://localhost:8080',
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
        },
        {
            path: '/recommendations',
            name: 'Recommendation',
            component: Recommendation,
            props: true,
        }
    ],
})