<template>
<div class="text-center">
    <base-input
          class="w-75"
          placeholder="password"
          v-model="password"
        >
        </base-input>
    <base-button type="primary" class="my-4" @click=trainNew>Train New</base-button>
    <base-button type="primary" class="my-4">Train Up</base-button>

    <base-button type="secondary" class="my-8">Disable System</base-button>

    <p v-if="incorrectPOST">{{logs}}</p>
    
</div>
</template>

<script>
import axios from "axios";
import {LEARN_URL, API_URL} from "../../axios-api.js";

export default {
    data () {
      return {
        password: "",
        logs: "",
        incorrectPOST: false,

        VolumeSpam: "",
        VolumeInbox: "",
        UsePredefinedModel: true,
      }
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
        trainNew (password) {
            let login = this.$store.username;

            axios({
                method: "POST",
                baseURL: LEARN_URL,
                url: "/create-model",
	


                data: {
                    email: this.$store.getters.username,
                    password: this.password,
                    inbox_volume: parseInt(this.VolumeInbox),
                    spam_volume: parseInt(this.VolumeSpam)
                },
                })
                .then((response) => {
                    
                    this.logs = "successful";
                    this.incorrectPOST = true;
                    
                })
                .catch((err) => {
                    this.logs = JSON.stringify(err);
                    console.log(err);
                    this.incorrectPOST = true;
                });
        }
    }
};
</script>
<style>
</style>
