import axios from 'axios';

function createInstanceWithAuth(url) {
  return axios.create({
    baseURL: `${process.env.VUE_APP_API_URL}${url}`,
  });
}
