<template>
  <div>
    <PageHeader :page-info="pageInfo" />
    <table
      v-if="tenants.length"
      class="table is-striped is-hoverable is-fullwidth"
    >
      <thead>
        <tr>
          <th>Adı - Soyadı</th>
          <th>T.C. Kimlik No.</th>
          <th>GSM</th>
          <th>E - Posta</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="t in tenants"
          :key="t.id"
          class="is-vcentered"
        >
          <td>{{ t.first_name }} {{ t.last_name }}</td>
          <td>{{ t.tc }}</td>
          <td>
            <the-mask
              class="input"
              disabled="disabled"
              :mask="['0### ### ####']"
              :value="t.gsm"
              type="tel"
            />
          </td>
          <td>{{ t.email }}</td>
          <td>
            <EntityActions
              :entity="t"
              :get-entity-list="getTenants"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import {TheMask} from 'vue-the-mask'
  import api from '../../clients/API'

  export default {
    name: 'TenantList',
    components: {
      TheMask,
    },
    data() {
      return {
        pageInfo: {
          title: 'Kiracılar',
          buttons: [
            {
              text: 'Yeni Kiracı',
              icon: 'fa fa-plus-circle',
              color: 'is-success',
              path_suffix: `${this.$route.path}/ekle`,
            },
          ],
        },
        tenants: [],
      }
    },
    mounted() {
      this.getTenants()
    },
    methods: {
      getTenants: async function () {
        this.tenants = await api.getTenants()
      }
    }
  }
</script>