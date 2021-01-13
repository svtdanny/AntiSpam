<template>
  <div class="col">
    <div class="row mt-3">
      <p class="h6">Use predifined model:</p>

      <base-checkbox v-model="UsePredefinedModel">
        <p></p>
      </base-checkbox>
    </div>
    <form v-on:submit.prevent="setSettings">
      <div class="row">
        <p class="h6">Train max volume Inbox:</p>
      </div>
      <div class="row">
        <base-input value='sd' v-model="VolumeInbox"> </base-input>
      </div>

      <div class="row">
        <p class="h6">Train max volume Spam:</p>
      </div>
      <div class="row">
        <base-input placeholder="this.VolumeSpam" v-model="VolumeSpam"> </base-input>
      </div>

      <div class="row">
        <base-button native-type="submit" type="primary" class="my-3" size="sm"
          >Save</base-button
        >
        <base-button tag="a" href="#/" type="secondary" class="my-3" size="sm"
          >Close</base-button
        >
      </div>
    </form>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

import {API_URL} from "../../axios-api.js";

export default {
  data() {
    return {
      VolumeSpam: "",
      VolumeInbox: "",
      UsePredefinedModel: true,

    };
  },

  created() {
    axios({
      method: "GET",
      url: API_URL + "/profile/learning_sets/",
      headers: {
        Authorization: `Token ${this.$store.state.accessToken}`,
      },
    })
      .then((response) => {
        this.VolumeInbox = response.data.VolumeInbox;
        this.VolumeSpam = response.data.VolumeSpam;
        this.UsePredefinedModel = response.data.UsePredefinedModel;
      })
      .catch((err) => {
        console.log(err);
      });
  },

  methods: {
    setSettings() {
      axios({
        method: "PUT",
        url: API_URL + "/profile/learning_sets/",
        headers: {
          Authorization: `Token ${this.$store.state.accessToken}`,
        },
        data: { VolumeInbox: this.VolumeInbox, VolumeSpam: this.VolumeSpam , UsePredefinedModel: this.UsePredefinedModel},
      }).catch((err) => {
        console.log(err);
      });
    },
  },
};
</script>
<style>
</style>
