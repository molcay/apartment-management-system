<template>
  <div
    v-if="landlord.length"
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
          v-for="l in landlord"
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
          <EntityActions :entity="l" />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import { TheMask } from 'vue-the-mask'
  import api from '../../clients/API'

  export default {
    name: 'LandlordList',
    components: {
      TheMask,
    },
    data() {
      return {
        pageInfo: {
          title: 'Mülk Sahipleri',
          button: {
            text: 'Yeni Mülk Sahibi',
            path_suffix: '/ekle',
          }
        },
        landlord: [],
      }
    },
    mounted() {
      this.getLandlords().then(landlord => {
        this.landlord = landlord
      })
    },
    methods: {
      getLandlords: () => {
        return api.getLandlords()
      }
    }
  }
</script>
