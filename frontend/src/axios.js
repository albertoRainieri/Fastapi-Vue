import axios from 'axios'

axios.defaults.baseURL = process.env.VUE_APP_BACKEND_URL + ':' + process.env.VUE_APP_BACKEND_PORT //'http://localhost:6000' ///process.env.BACKEND_URL //'http://localhost:6000/'
axios.defaults.headers.common['Authorization'] = 'Bearer' + localStorage.getItem['token']