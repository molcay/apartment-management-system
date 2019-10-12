<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput v-if="agreement.room">
      <template v-slot:labelElement>
        <label class="label">Oda</label>
      </template>
      <template v-slot:inputElement>
        <div class="input"> 
          {{ agreement.room.building_number }} / {{ agreement.room.home_number }} - {{ agreement.room.room_number }}
        </div>
      </template>
    </FormInput>

    <FormInput v-if="agreement.tenant">
      <template v-slot:labelElement>
        <label class="label">Kiracı</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.tenant.first_name }} {{ agreement.tenant.last_name }}({{ agreement.tenant.tc }})
        </div>
      </template>
    </FormInput>

    <FormInput v-if="agreement.guarantor">
      <template v-slot:labelElement>
        <label class="label">Kefil</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.guarantor.first_name }} {{ agreement.guarantor.last_name }}({{ agreement.tenant.tc }})
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kira Başlangıç Tarihi</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.start_date }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kira Bitiş Tarihi</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.end_date }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Kira Bedeli</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.lease_price }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Aidat Bedeli</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ agreement.dues }}
        </div>
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
        agreement: {},
        pageInfo: {
          title: 'Sözleşme Detayları',
          buttons: [
            {
              text: 'Dosyaları Oluştur',
              icon: 'far fa-file-word', //'fas fa-file-word',
              color: 'is-info',
              on_click: () => {
                this.createFiles(this.agreement.id)
              },
            },
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: `${this.$route.path.replace("detay","duzenle",)}`,
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
      },
      createFiles: (id) => {
        return api.createAgreementFiles(id);
      }
    },
  }
</script>
