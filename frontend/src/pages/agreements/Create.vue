<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Oda</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="agreement.room">
              <option value="-1">
                Oda Seçiniz
              </option>
              <option
                v-for="r in rooms"
                :key="r.id"
                :value="r"
                :selected="r===agreement.room"
              >
                {{ r.building_number }}/{{ r.home_number }}-{{ r.room_number }}
              </option>
            </select>
          </div>
        </template>
      </FormInput>
      
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Kiracının Adı-Soyadı</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="agreement.tenant">
              <option value="-1">
                Kiracı Adı-Soyadı Seçiniz
              </option>
              <option
                v-for="t in tenants"
                :key="t.id"
                :value="t"
                :selected="t===agreement.tenant"
              >
                {{ t.first_name }} {{ t.last_name }}({{ t.tc }})
              </option>
            </select>
          </div>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Kefilin Adı-Soyadı</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="agreement.guarantor">
              <option value="-1">
                Kefilin Adı-Soyadı
              </option>
              <option
                v-for="g in guarantors"
                :key="g.id"
                :value="g"
                :selected="g===agreement.guarantor"
              >
                {{ g.first_name }} {{ g.last_name }}({{ g.tc }})
              </option>
            </select>
          </div>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Kira Başlangıç Tarihi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="agreement.start_date"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            style="width:400px;"
            type="date"
            placeholder="Yıl-Ay-Gün (Örn:2020-01-01)"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Kira Bitiş Tarihi</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="agreement.end_date"
            class="input"
            :class="{'is-danger': errors && errors.end_date}"
            style="width:400px;"
            type="date"
            placeholder="Yıl-Ay-Gün (Örn:2020-01-01)"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Kira Bedeli</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="agreement.lease_price"
            class="input"
            :class="{'is-danger': errors && errors.lease_price}"
            style="width:400px;"
            type="number"
            placeholder="Kira Bedeli"
          >
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Aidat Bedeli</label>
        </template>
        <template v-slot:inputElement>
          <input
            v-model="agreement.dues"
            class="input"
            :class="{'is-danger': errors && errors.dues}"
            style="width:400px;"
            type="number"
            placeholder="Aidat Bedeli"
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
                @click="createAgreement"
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
import * as bulmaToast from "bulma-toast"


export default {
  name: "CreateAgreement",
  data() {
    return {
      agreement: {
        room: -1,
        tenant: -1,
        guarantor: -1
      },
      rooms: [],
      tenants: [],
      guarantors: [],
      errors: {},
      pageInfo: {
        title: "Yeni Sözleşme",
      }
    }
  },
  mounted() {

    this.getRooms().then(rooms => {
      this.rooms = rooms
    }),
    this.getTenants().then(tenants => {
      this.tenants = tenants
    }),
    this.getGuarantors().then(guarantors => {
      this.guarantors = guarantors
    })
  },
  methods: {
    
    getGuarantors: () => {
      return api.getGuarantors()
    },
    getRooms: () => {
      return api.getRooms()
    },
    getTenants: () => {
      return api.getTenants()
    },
    createAgreement: async function() {
      let errorMsg = ""

      if (
        this.agreement.lease_price &&
        Number(this.agreement.lease_price) <= 0
      ) {
        errorMsg = `Kira bedeli 0'dan büyük olmalıdır.`
      }

      if (this.agreement.dues && Number(this.agreement.dues) <= 0) {
        errorMsg = `Aidat bedeli 0'dan büyük olmalıdır.`
      }

      if (errorMsg) {
        bulmaToast.toast({
          message: errorMsg,
          type: "is-danger",
          position: "top-center",
          duration: 3000,
          dismissable: true
        })
      } else {
        const newAgreement = {
          room: this.agreement.room.id,
          tenant: this.agreement.tenant.id,
          guarantor: this.agreement.guarantor ? this.agreement.guarantor.id : null,
          start_date: this.agreement.start_date,
          end_date: this.agreement.end_date,
          lease_price: this.agreement.lease_price,
          dues: this.agreement.dues
        }
        const resp = await api.createAgreement(newAgreement)
        if (resp.status === 201) {
          return this.$router.push("/sozlesmeler")
        }
      }      
    }    
  }
}
</script>
