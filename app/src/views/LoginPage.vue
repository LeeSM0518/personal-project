<template>
  <v-app>
    <img
      src="../assets/loginicon.png"
      :class="`d-flex justify-center pa-10 mt-16`"
    />
    <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="submitLogin"
      lazy-validation
    >
      <div class="d-flex justify-center">
        <v-radio-group v-model="identity" row :rules="identityRules">
          <v-radio label="학생" value="student"></v-radio>
          <v-radio label="교수" value="professor"></v-radio>
        </v-radio-group>
      </div>

      <v-alert v-if="errorMessage" type="error" :class="`ml-15 mr-15`" dense>
        {{ errorMessage }}
      </v-alert>

      <v-text-field
        v-model="username"
        :rules="usernameRules"
        label="ID를 입력해 주세요."
        required
        :class="`pl-12 pr-12 ml-3 mr-3 mt-3`"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :rules="passwordRules"
        label="Password를 입력해 주세요."
        :class="`pl-12 pr-12 ml-3 mr-3`"
        type="password"
      ></v-text-field>

      <div class="d-flex justify-center mt-5 pl-15 pr-15">
        <v-btn
          type="submit"
          block=""
          :disabled="!valid"
          color="grey lighten-1"
          @click="validate"
        >
          로그인
        </v-btn>
      </div>
    </v-form>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    username: '',
    usernameRules: [v => !!v || 'ID를 반드시 입력해주세요.'],
    password: '',
    passwordRules: [v => !!v || 'Password를 반드시 입력해주세요.'],
    identity: '',
    identityRules: [v => !!v || '반드시 선택해주세요.'],
    errorMessage: '',
  }),

  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    async submitLogin() {
      try {
        const userData = {
          option: this.identity,
          username: this.username,
          password: this.password,
        };
        await this.$store.dispatch('LOGIN', userData);
        this.initLoginForm();
        if (this.identity === 'student') {
          this.$router.push('/student');
        } else {
          this.$router.push('/professor');
        }
      } catch (error) {
        this.errorMessage = error.response.data.message;
      }
    },
    initLoginForm() {
      this.username = '';
      this.password = '';
    },
  },
};
</script>

<style></style>
