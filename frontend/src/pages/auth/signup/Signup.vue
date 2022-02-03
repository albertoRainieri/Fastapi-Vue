<template>
  <form @submit.prevent="register()">

    <va-input
      class="mb-3"
      v-model="request.name"
      type="email"
      :label="$t('Full Name')"
      :error="!!nameErrors.length"
      :error-messages="nameErrors"
    />

    <va-input
      class="mb-3"
      v-model="request.age"
      type="integer"
      :label="$t('Age')"
      :error="!!ageErrors.length"
      :error-messages="ageErrors"
    />

    <va-input
      class="mb-3"
      v-model="request.email"
      type="email"
      :label="$t('auth.email')"
      :error="!!emailErrors.length"
      :error-messages="emailErrors"
    />

    <va-input
      class="mb-3"
      v-model="request.hashed_password"
      type="password"
      :label="$t('auth.password')"
      :error="!!passwordErrors.length"
      :error-messages="passwordErrors"
    />

    <va-input
      class="mb-3"
      v-model="request.confirm_password"
      type="password"
      :label="$t('Confirm Password')"
      :error="!!confirmPasswordErrors.length"
      :error-messages="confirmPasswordErrors"
    />

    <div class="auth-layout__options d-flex align--center justify--space-between">
      <va-checkbox
        v-model="agreedToTerms"
        class="mb-0"
        :error="!!agreedToTermsErrors.length"
        :errorMessages="agreedToTermsErrors"
      >
        <template #label>
          <span class="ml-1">
            {{ $t('auth.agree') }}
            <span class="link">{{ $t('auth.termsOfUse') }}</span>
          </span>
        </template>
      </va-checkbox>
      <router-link class="ml-1 link" :to="{name: 'recover-password'}">
        {{$t('auth.recover_password')}}
      </router-link>
    </div>

    <div class="d-flex justify--center mt-3">
      <va-button @click="register" class="my-0">{{ $t('auth.sign_up') }}</va-button>
    </div>
  </form>
</template>

<script>

import axios from 'axios';
import VueSweetalert2 from 'vue-sweetalert2';

export default {
  
  name: 'signup',
  data () {
    return {

      agreedToTerms: false,
      emailErrors: [],
      passwordErrors: [],
      confirmPasswordErrors: [],
      ageErrors: [],
      nameErrors: [],
      agreedToTermsErrors: [],
      request: {
        'name': '',
        'email': '',
        'age': '',
        'confirm_password': '',
        'hashed_password': ''
      }
    }
  },
  methods: {

    async register () {
      this.nameErrors = this.request.name ? [] : ['Name is required']
      this.ageErrors = this.request.age ? [] : ['Age is required']
      this.emailErrors = this.request.email ? [] : ['Email is required']
      this.passwordErrors = this.request.hashed_password ? [] : ['Password is required']
      this.confirmPasswordErrors = this.request.confirm_password ? [] : ['Password is required']
      this.agreedToTermsErrors = this.agreedToTerms ? [] : ['You must agree to the terms of use to continue']

      if (this.formReady) {
        let response = await axios.post('auth/register', this.request)
        let data = response.data;
        if (data.ack == 1) {
          this.$router.push({ name: 'dashboard' })
        }
      
      }
      
    }
  },
  computed: {
    formReady () {
      return !(this.ageErrors.length || this.nameErrors.length || this.emailErrors.length || this.passwordErrors.length || this.agreedToTermsErrors.length)
    },
  },
}
</script>

<style lang="scss">
</style>
