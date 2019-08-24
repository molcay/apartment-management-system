<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <FormInput>
      <template v-slot:labelElement>
        <label class="label">İsim</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.first_name }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Soyisim</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.last_name }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.address }}</option>
          </select>
        </div>
      </template>
    </FormInput>

       <FormInput>
      <template v-slot:labelElement>
        <label class="label">İş Adres</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.work_address }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Tc</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.tc }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">Telefon Numarası</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.gsm }}</option>
          </select>
        </div>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label class="label">E-Posta</label>
      </template>
      <template v-slot:inputElement>
        <div class="select">
          <select disabled>
            <option>{{ tenant.email }}</option>
          </select>
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
        tenant: null,
        pageInfo: {
          title: 'Mülk Sahipleri',
          buttons: [
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: '/duzenle',
            },
            {
              text: 'Sil',
              icon: 'fa fa-minus-circle',
              color: 'is-danger',
              path_suffix: '/duzenle',
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
