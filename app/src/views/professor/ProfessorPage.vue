<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $store.getters.getName }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn small @click="logout">로그아웃</v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <template>
          <v-card
            elevation="5"
            class="mx-auto"
            max-width="344"
            v-for="course in courses"
            :key="course.id"
            :class="`mb-5`"
            @click="linkMenu(course.id, course.title)"
          >
            <v-card-text>
              <p class="display-1 text--primary">
                {{ course.title }}
              </p>
              <div class="text--primary">분반 : {{ course._class }}</div>
              <div class="text--primary">강의요일 : {{ course.day }}</div>
              <div class="text--primary">
                강의실 : {{ course.dong }}동 {{ course.ho }}호
              </div>
              <div class="text--primary">
                강의시간 : {{ course.startTime.slice(0, 5) }} ~
                {{ course.endTime.slice(0, 5) }}
              </div>
            </v-card-text>
          </v-card>
        </template>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { fetchCourse } from '@/api/professor';

export default {
  data() {
    return {
      courses: [],
    };
  },
  methods: {
    async fetchData() {
      const { data } = await fetchCourse(this.$store.getters.getUserId);
      this.courses = data;
    },
    linkMenu(id, title) {
      this.$router.push({
        path: `/professor/courses/${id}`,
        query: { title: title },
      });
    },
    async logout() {
      await this.$store.commit('clearUser');
      this.$router.push('/login');
    },
  },
  created() {
    this.fetchData();
  },
};
</script>

<style></style>
