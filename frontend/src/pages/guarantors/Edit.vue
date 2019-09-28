<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form action="">
      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-first-name"
            class="label"
          >Ad</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.first_name"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.first_name"
            class="help is-danger"
          >
            {{ errors.first_name[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-last-name"
            class="label"
          >Soyad</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.last_name "
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.last_name"
            class="help is-danger"
          >
            {{ errors.last_name[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-tc"
            class="label"
          >T.C. Kimlik Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.tc "
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.tc"
            class="help is-danger"
          >
            {{ errors.tc[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-gsm"
            class="label"
          >Cep Telefonu</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.gsm"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.gsm"
            class="help is-danger"
          >
            {{ errors.gsm[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-address"
            class="label"
          >Adresi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.address "
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.address"
            class="help is-danger"
          >
            {{ errors.address[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-work-address"
            class="label"
          >İş Adresi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="guarantor.work_address "
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.work_address"
            class="help is-danger"
          >
            {{ errors.work_address[0] }}
          </p>
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
  name: "EditedGuarantor",
  data() {
    return {
      guarantor: {},
      errors: {},
      pageInfo: {
        title: "Kefiller",
        buttons: [
          {
            text: "Detay",
            icon: "fa fa-info-circle",
            color: "is-link",
            path_suffix: `${this.$route.path.replace("duzenle", "detay")}`
          },
        ]
      },
    }
  },
  mounted() {
    this.getDetails(this.$route.params.id).then(data => {
      this.guarantor = data
    })
  },
  methods: {
    getDetails: id => {
      return api.getGuarantor(id)
    },
    save: async function() {
      let errorMsg = ''

      if (this.guarantor.tc && this.guarantor.tc.length !== 11){
         errorMsg = `TC kimlik numarası 11 haneli olmalıdır.`
      }

      if (this.guarantor.gsm && this.guarantor.gsm.length !== 11){
        errorMsg = `GSM numarası 11 haneli olmalıdır.`
      }

      if (errorMsg) {
        bulmaToast.toast({
          message: errorMsg,
          type: 'is-danger',
          position: "top-center",
          duration: 3000,
          dismissible: true,
        })
      } else {
        const newGuarantor = {
          first_name: this.guarantor.first_name,
          last_name: this.guarantor.last_name,
          tc: this.guarantor.tc,
          gsm: this.guarantor.gsm,
          address: this.guarantor.address,
          work_address: this.guarantor.work_address
        }
        const resp = await api.saveGuarantor(this.guarantor.id, newGuarantor)
        if (resp.status === 200) {
          this.$router.push("/kefiller")
        }
      }
    }
  }
}
</script>
