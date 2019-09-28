<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Bina Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ room.building_number }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Ev Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ room.home_number }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Oda Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ room.room_number }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Boyut</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ room.size }}
        </div>
      </template>
    </FormInput>

    <FormInput v-if="room.landlord">
      <template v-slot:labelElement>
        <label class="label">Başlık/İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ room.landlord.title }}
        </div>
      </template>
    </FormInput>
  </div>
</template>


<script>
  import api from "../../clients/API"

export default {
  name: "DetailedRoom",
  data() {
    return {
      room: {},
      pageInfo: {
        title: "Odalar",
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
      this.room = data
    })
  },
  methods: {
    getDetails: id => {
      return api.getRoom(id)
    }
  }
}
</script>
