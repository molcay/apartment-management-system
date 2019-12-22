<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <PageHeader
      :page-info="pageInfo"
    />
    <div v-if="issue.created_by">
      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-first-name"
            class="label"
          >
            Kullanıcı Adı
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.created_by.username }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-last-name"
            class="label"
          >
            Arıza Tanımı
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.summary }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-tc"
            class="label"
          >
            Arıza Türü
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.issue_type }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-gsm"
            class="label"
          >
            Oluşturulma Tarihi
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.created_at }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-address"
            class="label"
          >
            Arıza Durumu
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.status }}
          </p>
        </template>
      </FormInput>

      <FormInput>
        <template v-slot:labelElement>
          <label
            for="field-work-address"
            class="label"
          >
            Arıza Geri Bildirimi
          </label>
        </template>
        <template v-slot:inputElement>
          <p
            class="input"
            disabled="disabled"
          >
            {{ issue.reply }}
          </p>
        </template>
      </FormInput>
    </div>
  </div>
</template>


<script>
  import api from "../../clients/API"

  export default {
    name: 'DetailedIssue',
    data() {
      return {
        issue: {},
        pageInfo: {
          title: 'Arıza Detayı',
          buttons: [
            {
              text: 'Düzenle',
              icon: 'fas fa-edit',
              color: 'is-warning',
              path_suffix: `${this.$route.path.replace("detay","duzenle",)}`
            },
          ],
        },
      }
    },
    mounted() {
      this.getDetails(this.$route.params.id).then(data => {
          this.issue = data
          var d = this.issue.created_at.slice(0, 10).split('-')
          this.issue.created_at = d[2] +'/'+ d[1] +'/'+ d[0]
      })
    },
    methods: {
      getDetails: (id) => {
        return api.getIssue(id)
      }
    },
  }
</script>
