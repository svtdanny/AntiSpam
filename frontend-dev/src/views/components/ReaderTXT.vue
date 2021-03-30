<template>
    <input type="file" @change="loadTextFromFile">
</template>

<script>
export default {
  methods: {
    loadTextFromFile(ev) {
      const file = ev.target.files[0];
      const reader = new FileReader();

      reader.onload = e => this.$emit("readAsText", e.target.result.replace(/(\r\n|\n|\r)/gm, ""));
      reader.readAsText(file);
    }
  }
};
</script>