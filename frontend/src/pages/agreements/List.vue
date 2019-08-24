<template>
  <div v-if="agreements.length">
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>#</th>
          <th>Oda</th>
          <th>Kiracı</th>
          <th>Başlangıç Tarihi</th>
          <th>Bitiş Tarihi</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="a in agreements"
          :key="a.id"
        >
          <td>{{ a.id }}</td>
          <td>{{ a.room.building_number }} / {{ a.room.home_number }} - {{ a.room.room_number }}</td>
          <td>{{ a.tenant.first_name }} {{ a.tenant.last_name }}</td>
          <td>{{ a.start_date }}</td>
          <td>{{ a.end_date }}</td>
          <EntityActions :entity="a" />
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import api from '../../clients/API'

  export default {
    name: 'AgreementList',
    data() {
      return {
        pageInfo: {
          title: 'Sözleşmeler',
          buttons: [
            {
              text: 'Yeni Sözleşme',
              icon: 'fa fa-plus-circle',
              color: 'is-success',
              path_suffix: `${this.$route.path}/ekle`,
            },
          ],
        },
        agreements: [],
      }
    },
    mounted() {
      this.getAgreements()
    },
    methods: {
      getAgreements: () => {
        return api.getAgreements()
      }
    }
  }
</script>

<style>
  td.is-flex {
    justify-content: space-evenly;
  }
</style>