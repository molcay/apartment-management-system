<template>
  <div class="tabs is-boxed">
    <ul>
      <li
        v-for="r in routes"
        :key="r.path"
        :class="{'is-active': $route.path.startsWith(r.path)}"
      >
        <router-link :to="r.path">
          <span class="icon is-small"><i :class="r.icon" /></span>
          <span>{{ r.text }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'Tabs',
    props: {
      routes: {
        type: Array,
        required: true,
        default: function () {
          return [
            {
              text: 'Ana Sayfa',
              path: '/',
              icon: 'fa fa-home',
            },
          ]
        },
      },
    },
  }
</script>