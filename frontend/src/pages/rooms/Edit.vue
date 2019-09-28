<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form>
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
          <div class="select">
            <select v-model="room.landlord">
              <option
                v-for="l in landlords"
                :key="l.id"
                :value="l"
                :selected="l===room.landlord"
              >
                {{ l.title }}
              </option>
            </select>
          </div>
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
                @click="saveRoom"
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
import * as bulmaToast from 'bulma-toast'


export default {
  name: "EditedRoom",
  data() {
    return {
      room: {},
      landlords: [],
      pageInfo: {
        title: "Odalar",
        buttons: [
          {
            text: "Detay",
            icon: "fa fa-info-circle",
            color: "is-link",
            path_suffix: `${this.$route.path.replace("duzenle", "detay")}`
          },
        ]
      },
      errors: {}
    }
  },
  mounted() {
    this.getDetails(this.$route.params.id).then(data => {
      this.room = data
    }),
    this.getLandlords().then(landlords => {
      this.landlords = landlords
    })
  },
  methods: {
    getDetails: id => {
      return api.getRoom(id)
    },
    getLandlords: () => {
      return api.getLandlords()
    },
    saveRoom: async function() {
      let errorMsg = ''
      
      if (this.room.tc && this.room.tc.length !==11 ){
        errorMsg = `TC kimlik numarası 11 haneli olmalıdır.`
      }
      

      if (this.room.gsm && this.room.gsm.length !=11 ) {
        errorMsg = `Oda numarası 1 haneli olmalıdır.`
      }

      if (errorMsg) {
        bulmaToast.toast({
          message: errorMsg,
          type: 'is-danger',
          position: "top-center",
          duration: 3000,
          dismissable: true
        })
      } else {
        const newRoom = {
          building_number: this.room.building_number,
          home_number: this.room.home_number,
          room_number: this.room.room_number,
          size: this.room.size,
          landlord: this.room.landlord.id
        }

        const resp = await api.saveRoom(this.room.id, newRoom)
        if (resp.status===200) {
          return this.$router.push("/odalar")
        }
      }
    }
  }
}
</script>
