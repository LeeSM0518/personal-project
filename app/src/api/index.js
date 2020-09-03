import axios from 'axios';

function createInstanceWithAuth(url) {
  return axios.create({
    baseURL: `${process.env.VUE_APP_API_URL}${url}`,
  });
}

const auth = createInstanceWithAuth('login');

function login(userData) {
  return auth.post('', userData);
}

export const student = createInstanceWithAuth('students');
export const professor = createInstanceWithAuth('professors');
export { login };
