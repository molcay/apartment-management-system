<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader :page-info="pageInfo" />
    <form>
      <FormInput>
        <template v-slot:labelElement>
          <label class="label">Bina Numarası</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="agreement.room">
              <option
                v-for="r in rooms"
                :key="r.id"
                :value="r"
                :selected="r===agreement.room"
              >
                {{ r.building_number }}
              </option>
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
            <select v-model="agreement.room">
              <option
                v-for="r in rooms"
                :key="r.id"
                :value="r"
                :selected="r===agreement.room"
              >
                {{ r.home_number }}
              </option>
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
            <select v-model="agreement.room">
              <option
                v-for="r in rooms"
                :key="r.id"
                :value="r"
                :selected="r===agreement.room"
              >
                {{ r.room_number }}
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

      <FormInput v-if="agreement.guarantor">
        <template v-slot:labelElement>
          <label class="label">Kefilin Adı-Soyadı</label>
        </template>
        <template v-slot:inputElement>
          <div class="select">
            <select v-model="agreement.guarantor">
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
            type="number"
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
            type="number"
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
                @click="saveAgreement"
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
  name: "EditedAgreement",
  data() {
    return {
      agreement: {},
      errors: {},
      rooms: [],
      tenants: [],
      guarantors: [],
      pageInfo: {
        title: "Sözleşme Detayları",
        buttons: [
          {
            text: "Dosyaları Oluştur",
            icon: "far fa-file-word", //'fas fa-file-word',
            color: "is-info",
            path_suffix: "/file"
          },
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
      this.agreement = data
    }),
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
    getDetails: id => {
      return api.getAgreement(id)
    },
    getGuarantors: () => {
      return api.getGuarantors()
    },
    getRooms: () => {
      return api.getRooms()
    },
    getTenants: () => {
      return api.getTenants()
    },
    saveAgreement: async function() {
      const newAgreement = {
        room: this.agreement.room.id,
        tenant: this.agreement.tenant.id,
        guarantor: this.agreement.guarantor ? this.agreement.guarantor.id : null,
        start_date: this.agreement.start_date,
        end_date: this.agreement.end_date,
        lease_price: this.agreement.lease_price,
        dues: this.agreement.dues
      }
      const resp = await api.saveAgreement(this.agreement.id, newAgreement)
      if (resp.status === 200) {
        return this.$router.push("/sozlesmeler")
      }      
    }    
  }
}
</script>
