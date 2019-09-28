<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div v-if="tenant">
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.first_name }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Soyisim</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.last_name }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.address }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">İş Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.work_address }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Tc</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.tc }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Telefon Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.gsm }}
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">E-Posta</label>
      </template>
      <template v-slot:inputElement>
        <div class="input">
          {{ tenant.email }}
        </div>
      </template>
    </FormInput>
  </div>
</template>


<script>
  import api from "../../clients/API"

  export default {
    name: 'DetailedTenant',
    data() {
      return {
        tenant: {},
        pageInfo: {
          title: 'Kiracılar',
          buttons: [
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
          this.tenant = data
        })
    },
    methods: {
      getDetails: (id) => {
        return api.getTenant(id)
      }
    },
  }
</script>
