
import axios from 'axios'

const API_URL = 'http://api.antispam-msu.site';

var getAPI = axios.create({
    baseURL: API_URL,
    timeout: 1000,
    headers: {
        "Content-type": "application/json"
      }
})




getAPI.defaults.xsrfHeaderName = "X-CSRFTOKEN"; getAPI.defaults.xsrfCookieName = "csrftoken";
getAPI.defaults.withCredentials = false;

//getAPI.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
export { getAPI, API_URL }