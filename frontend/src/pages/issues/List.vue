<template>
  <div>
    <PageHeader :page-info="pageInfo" />
    <table
      v-if="issues.length"
      class="table is-striped is-hoverable is-fullwidth"
    >
      <thead>
        <tr>
          <th>Kullanıcı Adı</th>
          <th>Arıza Tanımı</th>
          <th>Arıza Türü</th>
          <th>Oluşturulma Tarihi</th>
          <th>Arıza Durumu</th>
          <th>Arıza Geri Bildirimi</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="i in issues"
          :key="i.id"
        >
          <td>{{ i.created_by.username }}</td>
          <td>{{ i.summary }}</td>
          <td> {{ i.issue_type }} </td>
          <td> {{ i.created_at }} </td>
          <td> {{ i.status }} </td>
          <td> {{ i.reply }} </td>
          <td>
            <EntityActions
              :entity="i"
              :get-entity-list="getIssues"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import api from '../../clients/API'

  export default {
    name: 'IssueList',
    data() {
      return {
        pageInfo: {
          title: 'Arızalar',
        },
        issues: [],
      }
    },
    mounted() {
      this.getIssues()
    },
    methods: {
      getIssues: async function () {
        this.issues = await api.getIssues()
        for(var i=0;i<this.issues.length;i++){
          var d = this.issues[i].created_at.slice(0, 10).split('-')
          this.issues[i].created_at = d[2] +'/'+ d[1] +'/'+ d[0]
        }
      }
    }
  }
</script>