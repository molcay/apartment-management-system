<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-first-name"
          class="label"
        >
          Ad
        </label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.first_name }} </option>
          </select>
        </div>
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
        >
          Soyad
        </label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.last_name }} </option>
          </select>
        </div>
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
        >
          T.C. Kimlik Numarası
        </label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.tc }} </option>
          </select>
        </div>
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
        >
          Cep Telefonu
        </label>
      </template>
     <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.gsm }} </option>
          </select>
        </div>
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
        >
          Adresi
        </label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.address }} </option>
          </select>
        </div>
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
        >
          İş Adresi
        </label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option> {{ guarantor.work_address }} </option>
          </select>
        </div>
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
  </div>
</template>


<script>
  import api from "../../clients/API"

  export default {
    name: 'DetailedGuarantor',
    data() {
      return {
        guarantor: null,
        pageInfo: {
          title: 'Kefil Detayı',
          buttons: [
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: `${this.$route.path}/duzenle`,
            },
            {
              text: 'Sil',
              icon: 'fa fa-minus-circle',
              color: 'is-danger',
              path_suffix: `${this.$route.path}/sil`,
            },
          ],
        },
      }
    },
    mounted() {
      this.getDetails(this.$route.params.id).then(data => {
          this.guarantor = data
        })
    },
    methods: {
      getDetails: (id) => {
        return api.getGuarantor(id)
      }
    },
  }
</script>
