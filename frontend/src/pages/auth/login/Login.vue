<template>
  <form @submit.prevent="onsubmit">
    <va-input
      class="mb-3"
      v-model="form.email"
      type="email"
      :label="$t('auth.email')"
      :error="!!emailErrors.length"
      :error-messages="emailErrors"
    />

    <va-input
      class="mb-3"
      v-model="form.password"
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
        form: new Form({
        email: '',
        password: '',
        keepLoggedIn: false,
        emailErrors: [],
        passwordErrors: [],
      })
    }
  },
  computed: {
    formReady () {
      return !form.emailErrors.length && !form.passwordErrors.length
    },
  },
  methods: {
    test () {

    },
    onsubmit () {
      form.emailErrors = form.email ? [] : ['Email is required']
      form.passwordErrors = form.password ? [] : ['Password is required']
      if (!this.formReady) {
        return
      }
      this.$router.push({ name: 'dashboard' })
    },
    login () {
      this.form.post('http://localhost:5000/auth/login').then(response =>
        console.log(response)
      )
    }
  },
}
</script>
