<template>
  <div>
    <PageHeader :page-info="pageInfo" />
    <table v-if="rooms.length" class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>Oda</th>
          <th>Boyut(m<sup>2</sup>)</th>
          <th>Mülk Sahibi</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="r in rooms"
          :key="r.id"
        >
          <td>{{ r.building_number }} / {{ r.home_number }} - {{ r.room_number }}</td>
          <td>{{ r.size }}</td>
          <td>{{ r.landlord.title }}</td>
          <td><EntityActions
            :entity="r"
            :get-entity-list="getRooms"
          /></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import api from '../../clients/API'

  export default {
    name: 'RoomList',
    data() {
      return {
        pageInfo: {
          title: 'Odalar',
          buttons: [
            {
              text: 'Yeni Oda',
              icon: 'fa fa-plus-circle',
              color: 'is-success',
              path_suffix: `${this.$route.path}/ekle`,
            },
          ],
        },
        rooms: [],
      }
    },
    mounted() {
      this.getRooms()
    },
    methods: {
      getRooms: async function () {
        this.rooms = await api.getRooms()
      }
    }
  }
</script>