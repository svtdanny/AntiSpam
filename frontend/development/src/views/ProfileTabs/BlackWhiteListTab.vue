<template>
  <div class="row">
    <div class="col">
      <div class="row">
        <p class="h4">Delete</p>
      </div>
      <div class="row">
        <base-input
          class="w-75"
          placeholder="email(s) separated by commas"
          v-model="emailsToDelete"
        >
        </base-input>
      </div>
      <div class="row">
        <base-button type="primary" size="sm" @click="deleteFromMailLists"
          >Delete</base-button
        >
      </div>
      <br />

      <div class="row">
        <p class="h4">Add</p>
      </div>
      <div class="row">
        <base-input
          class="w-75"
          placeholder="email(s) separated by commas"
          v-model="inputList"
        >
        </base-input>
      </div>
      <div class="row">
        <base-button
          type="primary"
          size="sm"
          @click="addToMailLists(inputList, '')"
          >Add to White</base-button
        >
        <base-button
          type="primary"
          size="sm"
          @click="addToMailLists('', inputList)"
          >Add to Black</base-button
        >
      </div>
      <br />

      <div class="row">
        <p class="h4">Add from file</p>
      </div>
      <div class="row">
        <LoaderTXT @readAsText="loadedTextEmails = $event" />
      </div>
      <br />
      <div class="row">
        <select v-model="selectedList">
          <option disabled value="">Выберите список</option>
          <option>white</option>
          <option>black</option>
        </select>

        <base-button type="primary" size="sm" @click="addFromFile"
          >Add</base-button
        >
      </div>
    </div>

    <div class="col">
      <div class="row">
        <p class="h4">White list</p>
      </div>

      <div class="row">
        <ul class="list-unstyled">
          <li class="row-sm-3" v-for="addr in whiteList" :key="addr">
            {{ addr }}
          </li>
        </ul>
      </div>

      <div class="row mt-3">
        <p class="h4">Black list</p>
      </div>

      <div class="row">
        <ul class="list-unstyled">
          <li class="row-sm-3" v-for="addr in blackList" :key="addr">
            {{ addr }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BaseDropdown from "@/components/BaseDropdown.vue";
import LoaderTXT from "../components/ReaderTXT";

export default {
  components: {
    BaseDropdown,
    LoaderTXT,
  },
  created() {
    this.getMailLists();
  },
  data() {
    return {
      inputList: "",
      whiteList: [],
      blackList: [],

      emailsToDelete: "",

      loadedTextEmails: "",
      selectedList: "",

      checkboxes: {
        unchecked: false,
        checked: true,
        uncheckedDisabled: false,
        checkedDisabled: true,
      },
    };
  },
  methods: {
    getMailLists() {
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/profile/mail_lists/",
        headers: {
          Authorization: `Token ${this.$store.state.accessToken}`,
        },
      })
        .then((response) => {
          this.whiteList = response.data.whiteList.split(",");
          this.blackList = response.data.blackList.split(",");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addToMailLists(wh, bl) {
      if (wh) {
        var whParsed = wh.split(/(?:,| |;)+/);
        var blParsed = [];
      } else {
        var whParsed = [];
        var blParsed = bl.split(/(?:,| |;)+/);
      }
      axios({
        method: "PUT",
        url: "http://127.0.0.1:8000/profile/mail_lists/",
        headers: {
          Authorization: `Token ${this.$store.state.accessToken}`,
        },
        data: {
          whiteList: whParsed.join(),
          blackList: blParsed.join(),
        },
      })
        .then((response) => {
          this.whiteList = response.data.whiteList.split(",");
          this.blackList = response.data.blackList.split(",");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteFromMailLists() {
      axios({
        method: "DELETE",
        url: "http://127.0.0.1:8000/profile/mail_lists/",
        headers: {
          Authorization: `Token ${this.$store.state.accessToken}`,
        },
        data: {
          emailsToDelete: this.emailsToDelete.split(/(?:,| |;)+/).join(),
        },
      })
        .then((response) => {
          this.whiteList = response.data.whiteList.split(",");
          this.blackList = response.data.blackList.split(",");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addFromFile() {
      console.log(this.loadedTextEmails)
      if (this.selectedList == 'white'){
        this.addToMailLists(this.loadedTextEmails, "");
      }
      else{
        this.addToMailLists("", this.loadedTextEmails);
      }
    },
  },
};
</script>
<style>
</style>