<template>
    <div class="col">
    <div class="row mt-3">
        
            <p class='h6'>Use predifined model: {{VolumeSpam}}</p>

            <base-checkbox v-model="checkboxes.checked">
            <p></p>
            </base-checkbox>
    </div>
    <form v-on:submit.prevent="setSettings">
    <div class="row">
            <p class='h6'>Train max volume Inbox:</p>
    </div>
    <div class="row">
            <base-input placeholder="1..2000" v-model="VolumeInbox">
            </base-input>      
    </div>

    <div class="row">
            <p class='h6'>Train max volume Spam:</p>
    </div>
    <div class="row">
            <base-input placeholder="1..2000" v-model="VolumeSpam">
            </base-input>      
    </div>

    <div class="row">
        <base-button native-type="submit" type="primary" class="my-3" size=sm >Save</base-button>
        <base-button tag="a" href="#/" type="secondary" class="my-3" size=sm>Close</base-button>
    </div>
    </form>

    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
import { mapState } from 'vuex'
import axios from 'axios'

export default {
    data() {
    return {
        VolumeSpam: '',
        VolumeInbox: '',

      checkboxes: {
        unchecked: false,
        checked: true,
        uncheckedDisabled: false,
        checkedDisabled: true
      },
    }
    },
    
    created () {
        getAPI.get('/profile/LearnSets/', { headers: { Authorization: `Token ${this.$store.state.accessToken}` , 'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*"}})
          .then(response => {
            this.VolumeInbox = response.VolumeInbox
            this.VolumeSpam = response.VolumeSpam
          })
          .catch(err => {
            console.log(err)
          })
    },

    methods: {
        setSettings () { 
                axios({
                method: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/movies/',
                headers: {
                Authorization: `Token ${this.$store.state.accessToken}`
                },
                data: {title: "Ant Man and The Wasp", genre: "Action", year: 2018}
        }).catch(err => {
                console.log(err)    
                })
        }
        }

};


</script>
<style>
</style>
