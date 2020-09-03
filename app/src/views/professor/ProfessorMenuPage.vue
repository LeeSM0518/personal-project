<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $route.query.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn small @click="back">뒤로가기</v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <v-col style="margin-top: 50%">
          <v-row justify="center" align="center">
            <v-col>
              <v-btn x-large block class="pa-10 text-h4" @click="linkAttendance"
                >출석 확인</v-btn
              >
            </v-col>
          </v-row>
          <v-row justify="center" align="center">
            <v-col>
              <v-btn x-large block class="pa-10 text-h4" @click="linkSeats"
                >자리 확인</v-btn
              >
            </v-col>
          </v-row>
        </v-col>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  methods: {
    linkAttendance() {
      this.$router.push({
        path: `/professor/courses/${this.$route.params.id}/students`,
        query: { title: this.$route.query.title },
      });
    },
    linkSeats() {
      this.$router.push({
        path: `${this.$route.params.id}/seats`,
        query: { title: this.$route.query.title },
      });
    },
    back() {
      window.history.back();
    },
  },
};
</script>

<style></style>
