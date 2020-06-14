<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $router.params.title }}</v-toolbar-title>
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
  data() {
    return {
      attendances: [],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
        },
        {
          name: 'Eclair',
          calories: 262,
        },
        {
          name: 'Cupcake',
          calories: 305,
        },
        {
          name: 'Gingerbread',
          calories: 356,
        },
        {
          name: 'Jelly bean',
          calories: 375,
        },
        {
          name: 'Lollipop',
          calories: 392,
        },
        {
          name: 'Honeycomb',
          calories: 408,
        },
        {
          name: 'Donut',
          calories: 452,
        },
        {
          name: 'KitKat',
          calories: 518,
        },
      ],
    };
  },
  methods: {
    async fetchAttendances() {
      const userId = this.$store.getters.getUserId;
      const courseId = this.$route.params.id;
      const { data } = await fetchAttendances(userId, courseId);
      this.attendances = data;
    },
  },
  created() {
    this.fetchAttendances();
  },
};
</script>

<style></style>
