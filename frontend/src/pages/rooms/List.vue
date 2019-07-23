<template>
  <div v-if="rooms.length">
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
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
          <EntityActions :entity="r" />
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
      this.getRooms().then(rooms => {
        this.rooms = rooms
      })
    },
    methods: {
      getRooms: () => {
        return api.getRooms()
      }
    }
  }
</script>