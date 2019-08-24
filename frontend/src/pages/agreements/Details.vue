<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Oda</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ agreement.room.building_number }} / {{ agreement.room.home_number }} - {{ agreement.room.room_number }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kiracı</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ agreement.tenant.first_name }} {{ agreement.tenant.last_name }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput v-if="agreement.guarantor">
      <template v-slot:labelElement>
        <label class="label">Kefil</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ agreement.guarantor.first_name }} {{ agreement.guarantor.last_name }}</option>
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
          class="input"
          :class="{'is-danger': errors && errors.start_date}"
          type="date"
          :value="agreement.start_date"
          disabled
        >
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kira Bitiş Tarihi</label>
      </template>
      <template v-slot:inputElement>
        <input
          class="input"
          :class="{'is-danger': errors && errors.end_date}"
          type="date"
          :value="agreement.end_date"
          disabled
        >
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kira Bedeli</label>
      </template>
      <template v-slot:inputElement>
        <input
          class="input"
          :class="{'is-danger': errors && errors.lease_price}"
          type="number"
          :value="agreement.lease_price"
          disabled
        >
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Aidat Bedeli</label>
      </template>
      <template v-slot:inputElement>
        <input
          class="input"
          :class="{'is-danger': errors && errors.dues}"
          type="number"
          :value="agreement.dues"
          disabled
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
  </div>
</template>

<script>
  import api from '../../clients/API'

  export default {
    name: 'DetailedAgreement',
    data() {
      return {
        agreement: null,
        pageInfo: {
          title: 'Sözleşme Detayları',
          buttons: [
            {
              text: 'Dosyaları Oluştur',
              icon: 'far fa-file-word', //'fas fa-file-word',
              color: 'is-info',
              path_suffix: '/file',
            },
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: `${this.$route.path.replace("detay","duzenle",)}`,
            },
            {
              text: 'Sil',
              icon: 'fa fa-minus-circle',
              color: 'is-danger',
              path_suffix: `${this.$route.path.replace("detay","sil")}`,
            },
          ],
        },
      }
    },
    mounted() {
      this.getDetails(this.$route.params.id).then(data => {
          this.agreement = data
        })
    },
    methods: {
      getDetails: (id) => {
        return api.getAgreement(id)
      }
    },
  }
</script>
