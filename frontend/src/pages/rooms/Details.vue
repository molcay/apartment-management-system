<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div v-if="room">
    <PageHeader :page-info="pageInfo" />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Bina Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ room.building_number }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Ev Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ room.home_number }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Oda Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ room.room_number }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Boyut</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ room.size }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Başlık/İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ room.landlord.title }}</option>
          </select>
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
      room: null,
      pageInfo: {
        title: "Odalar",
        buttons: [
          {
            text: "Düzenle",
            icon: "fas fa-edit",
            color: "is-warning",
            path_suffix: `${this.$route.path.replace("detay", "duzenle")}`
          },
          {
            text: "Sil",
            icon: "fa fa-minus-circle",
            color: "is-danger",
            path_suffix: `${this.$route.path.replace("detay", "sil")}`
          }
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
