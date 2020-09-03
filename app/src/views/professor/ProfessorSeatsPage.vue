<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $route.query.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mr-5" small @click="updateData">자리 초기화</v-btn>
      <v-btn small @click="back">뒤로가기</v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <v-row justify="center" style="font-size: 10;" class="mt-10">
          <v-col
            cols="2"
            class="grey"
            style="text-align: center; padding-top: 50%;"
            >칠판</v-col
          >
          <v-col cols="9">
            <v-row v-for="(r, q) in row" :key="q" justify="center">
              <v-col v-for="(c, j) in col" :key="j">
                <v-btn
                  v-for="(s, i) in seat"
                  max-height="40"
                  max-width="10"
                  min-width="10"
                  :key="i"
                  ><div>
                    <div v-if="checkName()">
                      {{ seats[index].seatNumber }}
                    </div>
                    <div v-if="!checkName()" style="font-size: 10px;">
                      {{ seats[index].name }}{{ s }}
                    </div>
                    <div v-if="riseIndex()"></div></div
                ></v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-row justify="center" class="mt-10">
          <v-col
            cols="2"
            class="grey"
            style="font-size: 10; text-align: center;"
          >
            앞문
          </v-col>
          <v-col cols="6" style="font-size: 10; text-align: center;"> </v-col>
          <v-col
            cols="2"
            class="grey"
            style="font-size: 10; text-align: center;"
          >
            뒷문
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { fetchSeats, updateAllSeat } from '@/api/professor.js';

export default {
  data() {
    return {
      index: 0,
      row: ['', '', '', ''],
      col: ['', '', '', ''],
      seat: ['', ''],
      seats: [],
    };
  },
  methods: {
    back() {
      window.history.back();
    },
    async fetchData() {
      const { data } = await fetchSeats(
        this.$store.getters.getUserId,
        this.$route.params.courseId,
      );
      this.seats = data;
    },
    async updateData() {
      await updateAllSeat(
        this.$store.getters.getUserId,
        this.$route.params.courseId,
      );
      this.linkSeats();
    },
    riseIndex() {
      if (this.seats.length > this.index) {
        this.index += 1;
      }
      return false;
    },
    checkName() {
      const result =
        this.seats[this.index].name === '' ||
        this.seats[this.index].name === null;
      return result;
    },
    linkSeats() {
      this.$router.push({
        path: `.`,
        query: { title: this.$route.query.title },
      });
    },
  },
  computed: {},
  created() {
    this.fetchData();
  },
};
</script>

<style></style>
