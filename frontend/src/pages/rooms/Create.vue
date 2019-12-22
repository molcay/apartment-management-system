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
            style="width:500px;"
            type="text"
            placeholder="Bina Numarası"
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
            style="width:500px;"
            type="text"
            placeholder="Ev Numarası"
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
            style="width:500px;"
            type="text"
            placeholder="Oda Numarası"
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
            style="width:500px;"
            type="text"
            placeholder="Boyut"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Mülk Sahipleri</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="room.landlord">
              <option value="-1">
                Mülk Sahibi Seçiniz
              </option>
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
                @click="createRoom"
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
  name: "CreateRoom",
  data() {
    return {
      room: {
        landlord:-1
      },
      landlords: [],
      pageInfo: {
        title: "Odalar",
      },
      errors: {}
    }
  },
  mounted() {
    this.getLandlords().then(landlords => {
      this.landlords = landlords
    })
  },
  methods: {
    getLandlords: () => {
      return api.getLandlords()
    },
    createRoom: async function() {
      let errorMsg = ''
      
      if (this.room.building_number && this.room.building_number.length !==3 ){
        errorMsg = `Bina numarası 3 haneli olmalıdır.`
      }
      
      if (this.room.home_number && this.room.home_number.length !==1 && this.room.home_number.length !==2 ) {
        errorMsg = `Ev numarası 1 ya da 2 haneli olmalıdır.`
      }

      if (this.room.room_number && this.room.room_number.length !=1 ) {
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

        const resp = await api.createRoom(newRoom)
        if (resp.status===201) {
          return this.$router.push("/odalar")
        }
      }
    }
  }
}
</script>
