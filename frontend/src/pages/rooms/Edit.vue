<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form action>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Bina Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="room.building_number"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Ev Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="room.home_number"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Oda Numarası</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="room.room_number"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Boyut</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="room.size"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Başlık/İsim</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="room.landlord.title"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
          >
        </template>
      </FormInput>
      <div class="field is-horizontal">
        <div class="field-label">
          <!-- Left empty for spacing -->
        </div>
        <div class="field-body">
          <div class="field">
            <div class="control">
              <button
                class="button is-primary"
                :click="save()"
              >
                <span class="icon is-small">
                  <i class="fa fa-save" />
                </span>
                <span>Kaydet</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>


<script>
import api from "../../clients/API"

export default {
  name: "EditedRoom",
  data() {
    return {
      room: {},
      pageInfo: {
        title: "Odalar",
        buttons: [
          {
            text: "Detay",
            icon: "fa fa-info-circle",
            color: "is-link",
            path_suffix: `${this.$route.path.replace("duzenle", "detay")}`
          },
          {
            text: "Sil",
            icon: "fa fa-minus-circle",
            color: "is-danger",
            path_suffix: `${this.$route.path.replace("duzenle", "sil")}`
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
    },
    save() {
      const newRoom = {
        building_number: this.room.building_number,
        home_number: this.room.home_number,
        room_number: this.room.room_number,
        size: this.room.size,
        landlord: this.room.landlord,        
      }
      return api.saveRoom(this.room.id, newRoom)
    }
  }
}
</script>
