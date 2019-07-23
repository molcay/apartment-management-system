<template>
  <td class="is-flex">
    <router-link
      :to="`${$route.path}/${entity.id}/detay`"
      class="button is-link is-small"
    >
      <span class="icon is-small"><i class="fa fa-info-circle" /></span>
      <span>Detay</span>
    </router-link>
    <router-link
      :to="`${$route.path}/${entity.id}/${tr_to_ascii('düzenle')}`"
      class="button is-warning is-small"
    >
      <span class="icon is-small"><i class="fas fa-edit" /></span>
      <span>Düzenle</span>
    </router-link>
    <router-link
      :to="`${$route.path}/${entity.id}/sil`"
      class="button is-danger is-small"
    >
      <span class="icon is-small"><i class="fa fa-minus-circle" /></span>
      <span>Sil</span>
    </router-link>
  </td>
</template>

<script>
  import {tr_to_ascii} from "../helper"

  export default {
    name: 'EntityActions',
    props: {
      entity: {
        type: Object,
        required: true,
      }
    },
    methods: {
      tr_to_ascii,
    }
  }
</script>