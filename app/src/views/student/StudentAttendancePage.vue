<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $route.query.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn small @click="back">뒤로가기</v-btn>
    </v-app-bar>
    <v-simple-table :class="`mt-15`">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">주차</th>
            <th class="text-left">출석</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in attendances" :key="item.id">
            <td>{{ item.week }}</td>
            <td>{{ item.attendance }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-app>
</template>

<script>
import { fetchAttendances } from '@/api/student';

export default {
  props: {
    title: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      attendances: [],
    };
  },
  methods: {
    async fetchAttendances() {
      const userId = this.$store.getters.getUserId;
      const courseId = this.$route.params.id;
      const { data } = await fetchAttendances(userId, courseId);
      console.log(data);
      this.attendances = data;
    },
    back() {
      window.history.back();
    },
  },
  created() {
    this.fetchAttendances();
  },
};
</script>

<style></style>
