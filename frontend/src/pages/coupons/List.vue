<template>
  <div
    v-if="coupons.length"
    class="container"
  >
    <PageHeader :page-info="pageInfo" />
    <table class="table is-striped is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th>Kupon Kodu</th>
          <th>Kupon Süresi</th>
          <th>Veriliş Tarihi</th>
          <th>Son Kullanma Tarihi</th>
          <th>Verilen Kullanıcı</th>
          <th class="has-text-centered">
            Seçenekler
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="c in coupons"
          :key="c.id"
        >
          <td>{{ c.coupon_code }}</td>
          <td>{{ c.expire_in }}</td>
          <td>
            <p>{{ human_readable_date(c.started_at) }}</p>
          </td>
          <td>
            <p>{{ human_readable_date(c.expired_at) }}</p>
          </td>
          <td>{{ c.given_to.first_name + " " + c.given_to.last_name }}</td>
          <td>
            <EntityActions
              :entity="c"
              :get-entity-list="getCoupons"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import api from "../../clients/API"
  import {human_readable_date} from "../../helper"
  export default {
  name: "CouponList",
  data() {
    return {
      pageInfo: {
        title: "İnternet Erişim Kodları",
        buttons: [
          {
            text: "Yeni İnternet Erişim Kodu",
            icon: "fa fa-plus-circle",
            color: "is-success",
            path_suffix: `${this.$route.path}/ekle`
          }
        ]
      },
      coupons: []
    }
  },
  mounted() {
    this.getCoupons()
  },
  methods: {
    human_readable_date,
    getCoupons: async function () {
      this.coupons = await api.getCoupons()
    }
  }
}
</script>
