<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form action>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Başlık/İsim</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="landlord.title"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.title"
            class="help is-danger"
          >
            {{ errors.title[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Adres</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="landlord.address"
            class="input"
            :class="{'is-danger': errors && errors.address}"
            type="text"
            placeholder="Adres"
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
          <label class="label">Banka Bilgisi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="landlord.bank_info"
            class="input"
            :class="{'is-danger': errors && errors.bank_info}"
            type="text"
            placeholder="Banka Bilgisi"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.bank_info"
            class="help is-danger"
          >
            {{ errors.bank_info[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">IBAN</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="landlord.iban"
            class="input"
            :class="{'is-danger': errors && errors.iban}"
            type="text"
            placeholder="IBAN"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.iban"
            class="help is-danger"
          >
            {{ errors.iban[0] }}
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
import {tr_to_ascii} from "../../helper"
import api from "../../clients/API"

export default {
  name: "CreateLandlord",
  data() {
    return {
      landlord: {},
      errors: null,
      pageInfo: {
        title: "Mülk Sahipleri",        
      }
    }
  },
  mounted() {},
  methods: {
    getDetails: id => {
      return api.getLandlord(id)
    },
    save: async function () {
      const newLandLord = {
        title: this.landlord.title,
        address: this.landlord.address,
        bank_info: this.landlord.bank_info,
        iban: this.landlord.iban,
      }

      const resp = await api.createLandlord(newLandLord)
      if (resp.status === 201) {
        this.$router.push(tr_to_ascii("/mülk_sahipleri"))
      }
    } 
  }
}
</script>

