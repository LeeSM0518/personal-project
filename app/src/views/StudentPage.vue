<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{
        $store.getters.getName + ' ' + $store.getters.getUsername
      }}</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <template>
          <v-card
            class="mx-auto"
            max-width="344"
            v-for="course in courses"
            :key="course.id"
            :class="`mb-5`"
            @click="linkAttendances(course.id, course.title)"
          >
            <v-card-text>
              <p class="display-1 text--primary">
                {{ course.title }}
              </p>
              <p>{{ course.name }}</p>
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
import { fetchCourses } from '@/api/student';
export default {
  data() {
    return {
      courses: [],
    };
  },
  methods: {
    async fetchData() {
      const { data } = await fetchCourses(this.$store.getters.getUserId);
      this.courses = data;
    },
    linkAttendances(id, title) {
      this.$router.push({
        path: `/student/courses/${id}/attendance`,
        params: { title: title },
      });
    },
  },
  created() {
    this.fetchData();
  },
};
</script>

<style></style>
