import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router/router'

const app = createApp(App)

app.use(router)
    .use(ElementPlus)
    .use(VueAxios,axios)
    .mount('#app')
export default app