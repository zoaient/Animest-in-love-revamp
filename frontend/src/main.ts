import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from './router';
import 'vuetify/styles'
import vuetify from './plugins/vuetify'
import './assets/main.css'
import '@mdi/font/css/materialdesignicons.css' 

const app = createApp(App).use(router).use(vuetify); 

app.use(createPinia());

app.mount("#app");


