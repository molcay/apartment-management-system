<template>
  <div class="page-header">
    <span class="is-size-3">
      {{ pageInfo.title }}
    </span>
    <div
      v-if="pageInfo.buttons && pageInfo.buttons.length"
      class="buttons is-pulled-right"
    >
      <router-link
        v-for="btn in pageInfo.buttons"
        :key="btn.path_suffix"
        :to="btn.path_suffix"
        class="button"
        :class="btn.color"
      >
        <span class="icon is-small"><i :class="btn.icon" /></span>
        <span>{{ btn.text }}</span>
      </router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'PageHeader',
    props: {
      pageInfo: {
        type: Object,
        required: true,
        default() {
          return {
            title: 'Page Title',
            buttons: [
              {
                text: 'Button Text',
                icon: 'fa fa-plus-circle',
                color: 'is-success',
                path_suffix: '/yeni',
              },
              {
                text: 'Button Text 2',
                icon: 'fa fa-minus',
                color: 'is-success',
                path_suffix: '/yeni2',
              },
            ],
          }
        },
      },
    }
  }
</script>

<style>
  .page-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
</style>
