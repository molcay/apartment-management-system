<template>
  <div v-if="guarantors.length">
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>Adı - Soyadı</th>
          <th>T.C. Kimlik No.</th>
          <th>GSM</th>
          <th>Adresi</th>
          <th>İş Adresi</th>
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
          <td>{{ g.address }}</td>
          <td>{{ g.work_address }}</td>
          <EntityActions :entity="g" />
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
      this.getGuarantors().then(guarantors => {
        this.guarantors = guarantors
      })
    },
    methods: {
      getGuarantors: () => {
        return api.getGuarantors()
      }
    }
  }
</script>