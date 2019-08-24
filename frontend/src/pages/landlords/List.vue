<template>
  <div
    v-if="landlords.length"
    class="container"
  >
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>Mülk Sahibi</th>
          <th>Banka</th>
          <th>Adres</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="l in landlords"
          :key="l.id"
        >
          <td>{{ l.title }}</td>
          <td>
            <p>{{ l.bank_info }}</p>
            <p>
              <the-mask
                class="input"
                disabled="disabled"
                :mask="['TR## #### #### #### #### #### ##']"
                :value="l.iban"
                type="tel"
              />
            </p>
          </td>
          <td>{{ l.address }}</td>
          <EntityActions :entity="l" :getEntityList="getLandlords"/>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { TheMask } from "vue-the-mask"
import api from "../../clients/API"

export default {
  name: "LandlordList",
  components: {
    TheMask
  },
  data() {
    return {
      pageInfo: {
        title: "Mülk Sahipleri",
        buttons: [
          {
            text: "Yeni Mülk Sahibi",
            icon: "fa fa-plus-circle",
            color: "is-success",
            path_suffix: `${this.$route.path}/ekle`
          }
        ]
      },
      landlords: []
    }
  },
  mounted() {
    this.getLandlords()
  },
  methods: {
    getLandlords: async function () {
      console.log("getLandlords called")
      const landlords = await api.getLandlords()
      this.landlords = landlords
    }
  }
}
</script>
