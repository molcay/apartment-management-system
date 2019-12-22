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
          <div class="select">
            <select v-model="issue.status">
              <option
                v-for="i in issue_types"
                :key="i.id"
                :value="i"
                :selected="i===issue.status"
              >
                {{ i }}
              </option>
            </select>
          </div>
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
          <input
            v-model="issue.reply"
            class="input"
            :class="{'is-danger': errors && errors.title}"
            type="text"
            placeholder="Başlık/İsim"
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
                @click="save"
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
    </div>
  </div>
</template>


<script>
    import api from "../../clients/API"
    import * as bulmaToast from 'bulma-toast'


    export default {
        name: "EditedIssue",
        data() {
            return {
                issue: {},
                issue_types: ["Okundu", "Üzerinde Çalışılıyor", "Tamamlandı", "Redddedildi"],
                errors: {},
                pageInfo: {
                    title: "Arızalar",
                    buttons: [
                        {
                            text: "Detay",
                            icon: "fa fa-info-circle",
                            color: "is-link",
                            path_suffix: `${this.$route.path.replace("duzenle", "detay")}`
                        },
                    ]
                },
            }
        },
        mounted() {
            this.getDetails(this.$route.params.id).then(data => {
                this.issue = data
            })
        },
        methods: {
            getDetails: id => {
                return api.getIssue(id)
            },
            save: async function () {
                let errorMsg = ''

                if (this.issue.reply === "") {
                    errorMsg = `Geri dönüt mesajı boş olamaz`
                }

                if (errorMsg) {
                    bulmaToast.toast({
                        message: errorMsg,
                        type: 'is-danger',
                        position: "top-center",
                        duration: 3000,
                        dismissible: true,
                    })
                } else {
                    const newIssue = {
                        created_by: this.issue.created_by.id,
                        summary: this.issue.summary,
                        issue_type: this.issue.issue_type,
                        created_at: this.issue.created_at,
                        status: this.issue.status,
                        reply: this.issue.reply,
                    }
                    const resp = await api.saveIssue(this.issue.id, newIssue)
                    if (resp.status === 200) {
                        this.$router.push("/yonetim/arizalar")
                    }
                }
            }
        }
    }
</script>
