<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $route.query.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn small @click="back">뒤로가기</v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <v-row justify="center">
          <v-col>
            <v-data-table
              :headers="headers"
              :items="students"
              :search="search"
              sort-by="studentCode"
              class="elevation-1"
            >
              <template v-slot:top>
                <v-toolbar flat color="white">
                  <v-toolbar-title>출석 확인</v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>
                  <v-spacer></v-spacer>
                  <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    label="이름 검색"
                    single-line
                    hide-details
                  ></v-text-field>
                </v-toolbar>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-icon small class="mr-2" @click="linkAttendance(item)">
                  mdi-magnify
                </v-icon>
              </template>
              <template v-slot:no-data>
                <v-btn color="primary" @click="fetchData">Reset</v-btn>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { fetchStudentsInCourses } from '@/api/professor.js';

export default {
  data: () => ({
    dialog: false,
    search: '',
    headers: [
      {
        text: '학번',
        align: 'start',
        value: 'studentCode',
      },
      { text: '이름', value: 'name' },
      { text: '출석 점수', value: 'attendance' },
      { text: '자세히 보기', value: 'actions', sortable: false },
    ],
    students: [],
  }),

  created() {
    this.fetchData();
  },

  methods: {
    back() {
      window.history.back();
    },
    linkAttendance(student) {
      this.$router.push({
        path: `/professor/courses/${this.$route.params.id}/students/${student.id}/attendances`,
        query: { title: this.$route.query.title, name: student.name },
      });
    },
    async fetchData() {
      try {
        const { data } = await fetchStudentsInCourses(
          this.$store.getters.getUserId,
          this.$route.params.id,
        );
        this.students = data;
      } catch (error) {
        console.log(error.response.data.message);
      }
    },
  },
};
</script>

<style></style>
