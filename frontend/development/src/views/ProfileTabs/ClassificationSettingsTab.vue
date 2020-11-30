<template>
    <div class='col'>
    <div class="row mt-3">
    <p class='h6'>Define custom ISD spam filter strength</p>
    </div>
        
    <base-radio name="radioneg4" class="mb-3" v-model="ClassSetsRadio">
         Lenient (-0.4)
    </base-radio>

    <base-radio name="radioneg2" class="mb-3" v-model="ClassSetsRadio">
 	    Moderate (-0.2)
    </base-radio>

    <base-radio name="radioneg1" class="mb-3" v-model="ClassSetsRadio">
 	    Submoderate (-0.1)
    </base-radio>

    <base-radio name="radio3" class="mb-3" v-model="ClassSetsRadio">
 	    Normal (0.0)
    </base-radio>

    <base-radio name="radio1" class="mb-3" v-model="ClassSetsRadio">
 	    Subaggressive (0.1)
    </base-radio>

    <base-radio name="radio2" class="mb-3" v-model="ClassSetsRadio">
 	    Agressive (0.2)
    </base-radio>

    <base-radio name="radio4" class="mb-3" v-model="ClassSetsRadio">
 	    Exclusive (0.4)
    </base-radio>

    <div class="row mt-3">
    <p>It influes on probability of
        <ul>
        <li>false-positive error (normal correspondence is classified as spam); </li>
        <li>false-negative error (spam is classified as normal). </li>
        </ul>
    
    Lenient (-0.4) mode allows mimimize false-positive error <br>
    Exclusive (0.4) mode minimizes false-negative error</p>
    </div>
    
    <div class="row">
        <base-button type="primary" class="my-3" size=sm @click="saveClassSets">Save</base-button>
        <base-button tag="a" href="#/" type="secondary" class="my-3" size=sm>Close</base-button>
    </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  created() {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/profile/class_sets/",
      headers: {
        Authorization: `Token ${this.$store.state.accessToken}`,
      },
    })
      .then((response) => {
        this.ClassSetsRadio = response.data.ClassSetsRadio;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  data() {
    return {
      ClassSetsRadio: "radio3",
    };
  },
  methods: {
    saveClassSets() {
      let num = parseInt(this.ClassSetsRadio.slice(-1));

      num *= 0.1;

      if (this.ClassSetsRadio.slice(-4, -1) == "neg") {
        num *= -1;
      }

      axios({
        method: "PUT",
        url: "http://127.0.0.1:8000/profile/class_sets/",
        headers: {
          Authorization: `Token ${this.$store.state.accessToken}`,
        },
        data: {
          ClassSetsRadio: this.ClassSetsRadio,
          ClassSets: num,
        },
      }).catch((err) => {
        console.log(err);
      });
    },
  },
};
</script>
<style>
</style>
