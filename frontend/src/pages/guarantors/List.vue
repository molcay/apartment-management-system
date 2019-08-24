<template>
  <div v-if="guarantors.length">
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>Adı - Soyadı</th>
          <th>T.C. Kimlik No.</th>
          <th>GSM</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="g in guarantors"
          :key="g.id"
        >
          <td>{{ g.first_name }} {{ g.last_name }}</td>
          <td>{{ g.tc }}</td>
          <td>
            <the-mask
              class="input"
              disabled="disabled"
              :mask="['0### ### ####']"
              :value="g.gsm"
              type="tel"
            />
          </td>
          <EntityActions
            :entity="g"
            :get-entity-list="getGuarantors"
          />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import {TheMask} from 'vue-the-mask'
  import api from '../../clients/API'

  export default {
    name: 'GuarantorList',
    components: {
      TheMask,
    },
    data() {
      return {
        pageInfo: {
          title: 'Kefiller',
          buttons: [
            {
              text: 'Yeni Kefil',
              icon: 'fa fa-plus-circle',
              color: 'is-success',
              path_suffix: `${this.$route.path}/ekle`,
            },
          ],
        },
        guarantors: [],
      }
    },
    mounted() {
      this.getGuarantors()
    },
    methods: {
      getGuarantors: async function () {
        this.guarantors = await api.getGuarantors()
      }
    }
  }
</script>