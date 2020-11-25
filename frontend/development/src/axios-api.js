
import axios from 'axios'

var getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
    headers: {
        "Content-type": "application/json"
      }
})




getAPI.defaults.xsrfHeaderName = "X-CSRFTOKEN"; getAPI.defaults.xsrfCookieName = "csrftoken";
getAPI.defaults.withCredentials = false;

//getAPI.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
export { getAPI }