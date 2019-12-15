<template>
  <div class="page-header">
    <span class="is-size-3">
      {{ pageInfo.title }}
    </span>
    <div
      v-if="pageInfo.buttons && pageInfo.buttons.length"
      class="buttons is-pulled-right"
    >
      <button
        v-for="btn in buttons"
        :key="btn.click"
        class="button"
        :class="btn.color"
        @click="btn.on_click"
      >
        <span class="icon is-small"><i :class="btn.icon" /></span>
        <span>{{ btn.text }}</span>
      </button>
      <router-link
        v-for="link in links"
        :key="link.path_suffix"
        :to="link.path_suffix"
        class="button"
        :class="link.color"
      >
        <span class="icon is-small"><i :class="link.icon" /></span>
        <span>{{ link.text }}</span>
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
                on_click: null,
              },
              {
                text: 'Button Text 2',
                icon: 'fa fa-minus',
                color: 'is-success',
                on_click: () => {
                  alert("Clicked")
                },
              },
            ],
          }
        },
      },
    },
    computed: {
      links() {
        return this.pageInfo.buttons.filter((button) => !!button.path_suffix)
      },
      buttons() {
        return this.pageInfo.buttons.filter((button) => !!button.on_click)
      },
    },
  }
</script>

<style>
  .page-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
</style>
