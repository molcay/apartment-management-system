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
            type="text"
            placeholder="Başlık/İsim"
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
            type="text"
            placeholder="Başlık/İsim"
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
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">İş Adres</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.work_address"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Tc</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="tenant.tc"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
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
            type="text"
            placeholder="Başlık/İsim"
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
            type="text"
            placeholder="Başlık/İsim"
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
                @click="save"
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
    name: 'DetailedTenant',
    data() {
      return {
        tenant: {},
        errors:{},
        pageInfo: {
          title: 'Kiracılar',
          buttons: [
          {
            text: "Detay",
            icon: "fa fa-info-circle",
            color: "is-link",
            path_suffix: `${this.$route.path.replace("duzenle", "detay")}`
          },
          ],
        },
      }
    },
    mounted() {
      this.getDetails(this.$route.params.id).then(data => {
          this.tenant = data
        })
    },
    methods: {
      getDetails: (id) => {
        return api.getTenant(id)
      },
      save: async function(){
        let errorMsg = ''
      if (this.tenant.tc && this.tenant.tc.length !==11 ){
        errorMsg = `TC kimlik numarası 11 haneli olmalıdır.`
      }
      
      if (this.tenant.gsm && this.tenant.gsm.length !==11 ) {
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
          const resp = await api.saveTenant(this.tenant.id, newTenant)
          if(resp.status==200){
            return this.$router.push("/kiracilar")
          }
        }
      } 
    }
  }
</script>
