<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <form action="">
    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-first-name"
          class="label"
        >
          Ad
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-first-name"
          class="input"
          :class="{'is-danger': errors && errors.first_name}"
          type="text"
          placeholder="Ad (örn: Muhammed Olcay)"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.first_name"
          class="help is-danger"
        >
          {{ errors.first_name[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-last-name"
          class="label"
        >
          Soyad
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-last-name"
          class="input"
          :class="{'is-danger': errors && errors.last_name}"
          type="text"
          placeholder="Soyad (örn: TERCANLI)"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.last_name"
          class="help is-danger"
        >
          {{ errors.last_name[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-tc"
          class="label"
        >
          T.C. Kimlik Numarası
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-tc"
          class="input"
          :class="{'is-danger': errors && errors.tc}"
          type="text"
          minlength="11"
          maxlength="11"
          placeholder="T.C. Kimlik Numarası (örn: 12345678900)"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.tc"
          class="help is-danger"
        >
          {{ errors.tc[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-gsm"
          class="label"
        >
          Cep Telefonu
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-gsm"
          class="input"
          :class="{'is-danger': errors && errors.gsm}"
          type="text"
          minlength="11"
          maxlength="11"
          placeholder="Cep Telefonu (örn: 05301234567)"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.gsm"
          class="help is-danger"
        >
          {{ errors.gsm[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-email"
          class="label"
        >
          E-Posta
        </label>
      </template>
      <template v-slot:inputElement>
        <input
          id="field-email"
          class="input"
          :class="{'is-danger': errors && errors.email}"
          type="text"
          placeholder="E-Posta (örn: ad.soyad@domain.com)"
        >
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.email"
          class="help is-danger"
        >
          {{ errors.email[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-address"
          class="label"
        >
          Adresi
        </label>
      </template>
      <template v-slot:inputElement>
        <textarea
          id="field-address"
          class="textarea has-fixed-size"
          :class="{'is-danger': errors && errors.address}"
          placeholder="Ev Adresi"
          rows="3"
        />
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.address"
          class="help is-danger"
        >
          {{ errors.address[0] }}
        </p>
      </template>
    </FormInput>

    <FormInput>
      <template v-slot:labelElement>
        <label
          for="field-work-address"
          class="label"
        >
          İş Adresi
        </label>
      </template>
      <template v-slot:inputElement>
        <textarea
          id="field-work-address"
          class="textarea has-fixed-size"
          :class="{'is-danger': errors && errors.work_address}"
          placeholder="İş Adresi"
          rows="3"
        />
      </template>
      <template v-slot:helperText>
        <p
          v-if="errors && errors.work_address"
          class="help is-danger"
        >
          {{ errors.work_address[0] }}
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
  export default {
    name: 'CreateTenant',
    data() {
      return {
        fields: {},
        errors: {},
      }
    },
  }
</script>
