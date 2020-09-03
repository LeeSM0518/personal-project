<template>
  <v-app>
    <v-app-bar app color="grey lighten-2">
      <v-toolbar-title>{{ $route.query.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn small @click="back">뒤로가기</v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <v-data-table
          :headers="headers"
          :items="attendances"
          sort-by="week"
          :sort-desc="true"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-toolbar-title>{{ $route.query.name }}</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <span class="text-caption">(1: 출석, 0.5: 지각, 0: 결석)</span>
              <v-dialog v-model="dialog" max-width="500px">
                <v-card>
                  <v-card-title>
                    <span class="headline">출석 수정</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.week"
                            label="주차"
                            disabled
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="4">
                          <v-text-field
                            v-model="editedItem.attendance"
                            label="출석"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close"
                      >Cancel</v-btn
                    >
                    <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)">
              mdi-pencil
            </v-icon>
          </template>
          <template v-slot:no-data>
            <v-btn color="primary" @click="initialize">Reset</v-btn>
          </template>
        </v-data-table>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { fetchAttendanceByStudent, putAttendance } from '@/api/professor.js';

export default {
  data: () => ({
    dialog: false,
    headers: [
      {
        text: '주차',
        align: 'start',
        value: 'week',
      },
      { text: '출석', value: 'attendance' },
      { text: '', value: 'actions', sortable: false },
    ],
    attendances: [],
    editedIndex: -1,
    editedItem: {
      week: '',
      attendance: 0,
    },
    defaultItem: {
      week: '',
      attendance: 0,
    },
  }),

  watch: {
    dialog(val) {
      val || this.close();
    },
  },

  created() {
    this.initialize();
    this.fetchData();
  },

  methods: {
    back() {
      window.history.back();
    },

    initialize() {
      this.attendances = [
        {
          week: 1,
          attendance: 1,
        },
        {
          week: 2,
          attendance: 1,
        },
        {
          week: 3,
          attendance: 1,
        },
      ];
    },

    editItem(item) {
      this.editedIndex = this.attendances.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    async save() {
      Object.assign(this.attendances[this.editedIndex], this.editedItem);
      const result = await putAttendance(
        this.$store.getters.getUserId,
        this.$route.params.courseId,
        this.$route.params.studentId,
        this.editedItem,
      );
      this.close();
    },

    async fetchData() {
      const { data } = await fetchAttendanceByStudent(
        this.$store.getters.getUserId,
        this.$route.params.courseId,
        this.$route.params.studentId,
      );
      this.attendances = data;
    },
  },
};
</script>

<style></style>
