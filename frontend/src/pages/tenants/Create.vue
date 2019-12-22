<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <form action>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">İsim</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.first_name"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Soyisim</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.last_name"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="Soyisim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">T.C. Kimlik Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.tc"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="T.C. Kimlik Numarası"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Telefon Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.gsm"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="Telefon Numarası"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Adres</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.address"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="Adres"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">İş Adresi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.work_address"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="İş Adresi"
          >
        </template>
      </FormInput>


      <FormInput>
        <template v-slot:labelElement>
          <label class="label">E-Posta</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.email"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:500px;"
            type="text"
            placeholder="E-Posta"
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
  import api from "../../clients/API"
  import * as bulmaToast from 'bulma-toast'

  export default {
    name: 'CreateTenant',
    data() {
      return {
        tenant: {},
        errors:{},
        pageInfo: {
          title: 'Kiracılar',
        },
      }
    },
    methods: {
      create: async function(){
      let errorMsg = ''
      if (this.tenant.tc && this.tenant.tc.length !==11 ){
        errorMsg = `TC kimlik numarası 11 haneli olmalıdır.`
      }
      
      if (this.tenant.gsm && this.tenant.gsm.length !=11 ) {
        errorMsg = `GSM numarası 11 haneli olmalıdır.`
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

          const newTenant = {
            first_name: this.tenant.first_name,
            last_name: this.tenant.last_name,
            address: this.tenant.address,
            work_address: this.tenant.work_address,
            tc: this.tenant.tc,
            gsm: this.tenant.gsm,
            email: this.tenant.email,
          }

          const resp = await api.createTenant(newTenant)
          if(resp.status===201){
            return this.$router.push("/kiracilar")
          }
        }
      }
    }
  }
</script>
