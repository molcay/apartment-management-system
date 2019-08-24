<template>
  <div class="has-text-centered level">
    <router-link
      :to="`${$route.path}/${entity.id}/detay`"
      class="button is-link"
    >
      <span class="icon is-small"><i class="fa fa-info-circle" /></span>
      <span>Detay</span>
    </router-link>
    <router-link
      :to="`${$route.path}/${entity.id}/${tr_to_ascii('düzenle')}`"
      class="button is-warning"
    >
      <span class="icon is-smal"><i class="fas fa-edit" /></span>
      <span>Düzenle</span>
    </router-link>
    <a href="#" v-on:click="deleteEntity()" class="button is-danger has-text-right">
      <span class="icon is-small is-right"><i class="fa fa-minus-circle" /></span>
      <span>Sil</span>
    </a>
  </div>
</template>

<script>
  import {tr_to_ascii} from "../helper"
  import api from "../clients/API"

  export default {
    name: 'EntityActions',
    props: {
      entity: {
        type: Object,
        required: true,
      },
      getEntityList: {
        type: Function,
        required: true,
      },
    },
    methods: {
      tr_to_ascii,
      deleteEntity() {
        let deleteFun
        switch(this.$route.path) {
          case tr_to_ascii('/mülk_sahipleri'):
            deleteFun = api.deleteLandlord
            break
          case tr_to_ascii('/kiracılar'):
            deleteFun = api.deleteTenant
            break
          case tr_to_ascii('/odalar'):
            deleteFun = api.deleteRoom
            break
          case tr_to_ascii('/kefiller'):
            deleteFun = api.deleteGuarantor
            break
          case tr_to_ascii('/sözleşmeler'):
            deleteFun = api.deleteAgreement
            break
          default:
            break
        }

        deleteFun(this.entity.id).then((resp) => {
          if (resp.status === 204) {
            this.getEntityList()
          } else {
            console.error(resp)
          }
        })
      },
    }
  }
</script>