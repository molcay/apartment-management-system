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
            v-model="newUser.username"
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
          <label class="label">E-posta</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="newUser.email"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="E-posta"
          >
        </template>
      </FormInput>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Parola</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="newUser.password"
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
    name: 'SignUp',
    data() {
      return {
        newUser: {},
        errors:{},
        pageInfo: {
          title: 'Kullanıcı Oluştur',
        },
      }
    },
    methods: {
      create: async function(){
      let errorMsg = ''
      if (this.newUser.tc && this.newUser.tc.length !==11 ){
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

          const resp = await api.createUser(this.newUser)
          if(resp.status===201){
            return this.$router.push("/giris")
          }
        }
      }
    }
  }
</script>
