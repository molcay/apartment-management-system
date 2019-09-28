<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Başlık/İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">          
          {{ landlord.title }}          
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ landlord.address }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Banka Bilgisi</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ landlord.bank_info }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">IBAN</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ landlord.iban }}
        </div>
      </template>
    </FormInput>
  </div>
</template>


<script>
import api from "../../clients/API"

export default {
  name: "DetailedLandlord",
  data() {
    return {
      landlord: {},
      pageInfo: {
        title: "Mülk Sahipleri",
        buttons: [
          {
            text: "Düzenle",
            icon: "fas fa-edit",
            color: "is-warning",
            path_suffix: `${this.$route.path.replace("detay", "duzenle")}`
          },
        ]
      }
    }
  },
  mounted() {
    this.getDetails(this.$route.params.id).then(data => {
      this.landlord = data
    })
  },
  methods: {
    getDetails: id => {
      return api.getLandlord(id)
    }
  }
}
</script>
