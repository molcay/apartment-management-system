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
        <div class="input">
          {{ guarantor.first_name }}
        </div>
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
        <div class="input">
          {{ guarantor.last_name }}
        </div>
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
        <div class="input">
          {{ guarantor.tc }}
        </div>
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
        <div class="input">
          {{ guarantor.gsm }}
        </div>
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
        <div class="input">
          {{ guarantor.address }}
        </div>
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
        <div class="input">
          {{ guarantor.work_address }}
        </div>
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
        guarantor: {},
        pageInfo: {
          title: 'Kefil Detayı',
          buttons: [
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: `${this.$route.path.replace("detay","duzenle",)}`
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
