<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <form action="">
    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-building-number"
          class="label"
        >
          Bina numarası
        </label>
      </template>
      <template v-slot:inputElement>
        <div
          class="select"
          :class="{'is-danger': errors && errors.building_number}"
        >
          <select
            id="field-building-number"
            v-model="fields.building_number"
          >
            <option value="-1">
              Bina Numarası Seç
            </option>
            <option
              v-for="building in buildings"
              :key="building"
              :value="building"
            >
              {{ building }}
            </option>
          </select>
        </div>
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.building_number"
          class="help is-danger"
        >
          {{ errors.building_number[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-home-number"
          class="label"
        >
          Ev Kapı Numarası
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-home-number"
          class="input"
          :class="{'is-danger': errors && errors.home_number}"
          type="text"
          placeholder="Ev Kapı Numarası"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.home_number"
          class="help is-danger"
        >
          {{ errors.home_number[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-room-number"
          class="label"
        >
          Oda Numarası
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-room-number"
          class="input"
          :class="{'is-danger': errors && errors.room_number}"
          type="text"
          placeholder="Oda Numarası"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.room_number"
          class="help is-danger"
        >
          {{ errors.room_number[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-size"
          class="label"
        >
          Boyut (m<sup>2</sup>)
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-size"
          class="input"
          :class="{'is-danger': errors && errors.size}"
          type="text"
          placeholder="Boyut"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.size"
          class="help is-danger"
        >
          {{ errors.size[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-landlord"
          class="label"
        >
          Mülk Sahibi
        </label>
      </template>
      <template v-slot:inputElement>
        <div
          class="select"
          :class="{'is-danger': errors && errors.landlord}"
        >
          <select
            id="field-landlord"
            v-model="fields.landlord"
          >
            <option value="-1">
              Mülk Sahibi seç
            </option>
            <option
              v-for="l in landlords"
              :key="l.id"
              :value="l.id"
            >
              {{ l.title }}
            </option>
          </select>
        </div>
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.landlord"
          class="help is-danger"
        >
          {{ errors.landlord[0] }}
        </p>
      </template>
    </FormInput>

    <div class="field is-horizontal">
      <div class="field-label">
        <!-- Left empty for spacing -->
      </div>
      <div class="field-body">
        <div class="field">
          <div class="control">
            <button class="button is-primary">
              <span class="icon is-small"><i class="fa fa-save" /></span>
              <span>Kaydet</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
  import LandlordService from '../../services/LandlordService'

  export default {
    name: 'CreateRoom',
    data() {
      return {
        buildings: ['110', '112'],
        landlords: [],
        fields: {
          building_number: -1,
          landlord: -1,
        },
        errors: {},
      }
    },
    mounted() {
      LandlordService.getAll().then(landlords => {
        this.landlords = landlords
      })
    }
  }
</script>
