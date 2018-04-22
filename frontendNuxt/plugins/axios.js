import axios from 'axios'
import Vue from 'vue'


axios.defaults.timeout = 5000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.baseURL = "http://127.0.0.1:8000/api/"

export default axios

