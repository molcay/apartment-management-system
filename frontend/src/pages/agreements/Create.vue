<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="{title: 'Yeni Sözleşme'}" />
    <form action="">
      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-room"
            class="label"
          >
            Oda
          </label>
        </template>
        <template v-slot:inputElement>
          <div
            class="select"
            :class="{'is-danger': errors && errors.room}"
          >
            <select
              id="field-room"
              v-model="fields.room"
            >
              <option value="-1">
                Oda seç
              </option>
              <option
                v-for="room in rooms"
                :key="room.id"
                :value="room.id"
              >
                {{ room.name }}
              </option>
            </select>
          </div>
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.room"
            class="help is-danger"
          >
            {{ errors.room[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-tenant"
            class="label"
          >
            Kiracı
          </label>
        </template>
        <template v-slot:inputElement>
          <div
            class="select"
            :class="{'is-danger': errors && errors.tenant}"
          >
            <select
              id="field-tenant"
              v-model="fields.tenant"
            >
              <option value="-1">
                Kiracı seç
              </option>
              <option
                v-for="tenant in tenants"
                :key="tenant.id"
                :value="tenant.id"
              >
                {{ tenant.full_name }}
              </option>
            </select>
          </div>
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.tenant"
            class="help is-danger"
          >
            {{ errors.tenant[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-guarantor"
            class="label"
          >
            Kefil
          </label>
        </template>
        <template v-slot:inputElement>
          <div
            class="select"
            :class="{'is-danger': errors && errors.guarantor}"
          >
            <select
              id="field-guarantor"
              v-model="fields.guarantor"
            >
              <option value="-1">
                Kefil seç
              </option>
              <option
                v-for="guarantor in guarantors"
                :key="guarantor.id"
                :value="guarantor.id"
              >
                {{ guarantor.first_name }}
                {{ guarantor.last_name }}
              </option>
            </select>
          </div>
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.guarantor"
            class="help is-danger"
          >
            {{ errors.guarantor[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-start-date"
            class="label"
          >
            Kira Başlangıç Tarihi
          </label>
        </template>
        <template v-slot:inputElement>
          <input
            id="field-start-date"
            class="input"
            :class="{'is-danger': errors && errors.start_date}"
            type="date"
            placeholder="Kira Başlangıç Tarihi"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.start_date"
            class="help is-danger"
          >
            {{ errors.start_date[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-end-date"
            class="label"
          >
            Kira Bitiş Tarihi
          </label>
        </template>
        <template v-slot:inputElement>
          <input
            id="field-end-date"
            class="input"
            :class="{'is-danger': errors && errors.end_date}"
            type="date"
            placeholder="Kira Bitiş Tarihi"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.end_date"
            class="help is-danger"
          >
            {{ errors.end_date[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-lease-price"
            class="label"
          >
            Kira Bedeli
          </label>
        </template>
        <template v-slot:inputElement>
          <input
            id="field-lease-price"
            class="input"
            :class="{'is-danger': errors && errors.lease_price}"
            type="number"
            placeholder="Kira Bedeli"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.lease_price"
            class="help is-danger"
          >
            {{ errors.lease_price[0] }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-dues"
            class="label"
          >
            Aidat Bedeli
          </label>
        </template>
        <template v-slot:inputElement>
          <input
            id="field-dues"
            class="input"
            :class="{'is-danger': errors && errors.dues}"
            type="number"
            placeholder="Aidat Bedeli"
          >
        </template>
        <template v-slot:helperText>
          <p
            v-if="errors && errors.dues"
            class="help is-danger"
          >
            {{ errors.dues[0] }}
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
  </div>
</template>

<script>
  import GuarantorService from '../../services/GuarantorService'
  import TenantService from '../../services/TenantService'
  import RoomService from '../../services/RoomService'


  export default {
    name: 'CreateAgreement',
    data() {
      return {
        rooms : [],
        tenants : [],
        guarantors: [],
        fields: {
          room: -1,
          tenant: -1,
          guarantor: -1,
        },
        errors: {},
      }
    },
    mounted() {
      const promiseList = [RoomService, TenantService, GuarantorService].map(service => service.getAll())

      Promise.all(promiseList).then(([rooms, tenants, guarantors]) => {
        this.rooms = rooms
        this.tenants = tenants
        this.guarantors = guarantors
      })
    }
  }
</script>
