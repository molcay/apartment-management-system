<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Başlık/İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ landlord.title }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ landlord.address }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Banka Bilgisi</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ landlord.bank_info }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">IBAN</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ landlord.iban }}</option>
          </select>
        </div>
      </template>
    </FormInput>
  </div>
</template>


<script>
  import api from "../../clients/API"

  export default {
    name: 'DetailedLandlord',
    data() {
      return {
        landlord: null,
        pageInfo: {
          title: 'Mülk Sahipleri',
          buttons: [
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: '/duzenle',
            },
            {
              text: 'Sil',
              icon: 'fa fa-minus-circle',
              color: 'is-danger',
              path_suffix: '/duzenle',
            },
          ],
        },
      }
    },
    mounted() {
      this.getDetails(this.$route.params.id).then(data => {
          this.landlord = data
        })
    },
    methods: {
      getDetails: (id) => {
        return api.getLandlord(id)
      }
    },
  }
</script>
