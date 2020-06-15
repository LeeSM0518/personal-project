import Vue from 'vue';
import Vuex from 'vuex';
import { login } from '@/api/index';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: -1,
    name: '',
    username: '',
  },
  getters: {
    getUserId(state) {
      return state.userId;
    },
    getName(state) {
      return state.name;
    },
    getUsername(state) {
      return state.username;
    },
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    },
    setUserId(state, userId) {
      state.userId = userId;
    },
    setUsername(state, username) {
      state.username = username;
    },
  },
  actions: {
    async LOGIN({ commit }, userData) {
      const { data } = await login(userData);
      commit('setName', data.name);
      commit('setUserId', data.id);
      commit('setUsername', userData.username);
    },
  },
  modules: {},
});
