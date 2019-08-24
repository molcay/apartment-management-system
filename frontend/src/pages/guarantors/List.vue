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
          <td>{{ g.gsm }}</td>
          <EntityActions :entity="g" :getEntityList="getGuarantors"/>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import api from '../../clients/API'

  export default {
    name: 'GuarantorList',
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
        console.log("getGuarantors called")
        const guarantors = await api.getGuarantors()
        this.guarantors = guarantors
        
      }
    }
  }
</script>