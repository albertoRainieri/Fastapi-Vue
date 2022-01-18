<template>
  <form @submit.prevent="login">
    <va-input
      class="mb-3"
      v-model="requestLogin.email"
      type="email"
      :label="$t('auth.email')"
      :error="!!emailErrors.length"
      :error-messages="emailErrors"
    />

    <va-input
      class="mb-3"
      v-model="requestLogin.hashed_password"
      type="password"
      :label="$t('auth.password')"
      :error="!!passwordErrors.length"
      :error-messages="passwordErrors"
    />

    <div class="auth-layout__options d-flex align--center justify--space-between">
      <va-checkbox v-model="keepLoggedIn" class="mb-0" :label="$t('auth.keep_logged_in')"/>
      <router-link class="ml-1 link" :to="{name: 'recover-password'}">{{$t('auth.recover_password')}}</router-link>
    </div>

    <div class="d-flex justify--center mt-3">
      <va-button @click.native="login" class="my-0">{{ $t('auth.login') }}</va-button>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  data () {
    return {
      keepLoggedIn: false,
      emailErrors: [],
      passwordErrors: [],

      requestLogin: {
        'email': '',
        'hashed_password': ''
      }
    }
  },
  computed: {
    formReady () {
      return !this.emailErrors.length && !this.passwordErrors.length
    },
  },

  methods: {
    async login () {
      this.emailErrors = this.requestLogin.email ? [] : ['Email is required']
      this.passwordErrors = this.requestLogin.hashed_password ? [] : ['Password is required']
      
      if (this.formReady) {
        const response = await axios.post('auth/login', this.requestLogin)
        if (response.data.ack == 1) {
          localStorage.setItem('token', response.data.token) 
          this.$router.push({ name: 'dashboard'})
        }
      }
    }
}}
</script>