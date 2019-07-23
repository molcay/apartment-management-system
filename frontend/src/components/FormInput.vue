<template>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <slot name="labelElement"></slot>
    </div>
    <div class="field-body">
      <div class="field">
        <div class="control">
          <slot name="inputElement" />
        </div>
        <slot name="helperText" />
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'FormInput',
  }
</script>