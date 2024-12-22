import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const toastOptions = {
    // You can set your default options here
};


createApp(App)
    .use(Toast, toastOptions)
    .use(VueSweetalert2)
    .mount('#app')
