<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form action>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">T.C. Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="userLogin.username"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="T.C. Numarası"
          >
        </template>
      </FormInput>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Parola</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="userLogin.password"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="password"
            placeholder="Parola"
          >
        </template>
      </FormInput>
      <div class="field is-horizontal">
        <div class="field-label">
          <!-- Left empty for spacing -->
        </div>
        <div class="field-body">
          <div class="field">
            <div class="control">
              <button
                class="button is-primary"
                @click="create"
              >
                <span class="icon is-small">
                  <i class="fa fa-save" />
                </span>
                <span>Kaydet</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
  import api from "../../clients/AuthAPI"
  import * as bulmaToast from 'bulma-toast'

  export default {
    name: 'Login',
    data() {
      return {
        userLogin: {},
        errors:{},
        pageInfo: {
          title: 'Sisteme giriş yap',
        },
      }
    },
    methods: {
      create: async function(){
      let errorMsg = ''
      if (this.userLogin.tc && this.userLogin.tc.length !==11 ){
        errorMsg = `TC kimlik numarası 11 haneli olmalıdır.`
      }

      if (errorMsg) {
        bulmaToast.toast({
          message: errorMsg,
          type: 'is-danger',
          position: "top-center",
          duration: 3000,
          dismissable: true
        })
      } else {

          const resp = await api.loginUser(this.userLogin)
          if(resp.status===200){
            const token = resp.data.auth_token
            localStorage.setItem("token", token)
            return this.$router.push("/")
          }
        }
      }
    }
  }
</script>
