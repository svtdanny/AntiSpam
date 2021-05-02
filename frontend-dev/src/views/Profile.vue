<template>
  <div class="profile-page">
    <section class="section section-skew">
      <div class="row justify-content-center">
        <div class="col-lg-6">
          <!-- Tabs with icons -->
          <tabs fill class="flex-column flex-md-row">
            <card shadow slot-scope="{ activeTabIndex }">
              <tab-pane key="tab1">
                <template slot="title"> Train </template>
                <LearningTab></LearningTab>
              </tab-pane>

              <tab-pane key="tab2">
                <template slot="title"> Learning settings </template>

                <LearningSettingsTab></LearningSettingsTab>
              </tab-pane>

              <tab-pane key="tab3" v-if="false">
                <template slot="title"> Classification settings </template>

                <ClassificationSettingsTab></ClassificationSettingsTab>
              </tab-pane>

              <tab-pane key="tab4">
                <template slot="title"> White and Black lists </template>
                <BlackWhiteListTab></BlackWhiteListTab>
              </tab-pane>
            </card>
          </tabs>
        </div>
        <div class="col-lg-4">
          <br />
          <h1 class="display-4">Statistics</h1>
          <div>
            <p class="h4">Current status</p>
          </div>

          <div class="row justify-content-left">
            <div class="col-lg-4">
              <p class="h6">Prev. operation info</p>
            </div>
            <div class="col-lg-4">
              <p>OK</p>
            </div>
          </div>

          <div>
            <p class="h4">Totals</p>
          </div>

          <div class="row justify-content-left">
            <div class="col-lg-4">
              <p class="h6">Last train</p>
            </div>
            <div class="col-lg-4">
              <p>{{lastLearn}}</p>
            </div>
          </div>
          <div class="row justify-content-left">
            <div class="col-lg-4">
              <p class="h6">Total time</p>
            </div>
            <div class="col-lg-4">
              <p>{{totalTime}}</p>
            </div>
          </div>
          <div class="row justify-content-left">
            <div class="col-lg-4">
              <p class="h6">Inbox used:</p>
            </div>
            <div class="col-lg-4">
              <p>{{VolumeInbox}}</p>
            </div>
          </div>
          <div class="row justify-content-left">
            <div class="col-lg-4">
              <p class="h6">Spam used:</p>
            </div>
            <div class="col-lg-4">
              <p>{{VolumeSpam}}</p>
            </div>
          </div>

          <div v-if="false">
            <p class="h4">TrainUp's history</p>
          </div>
          <div class="row justify-content-left" v-if="false">
            <div class="col-lg-8">
              <p class="h6">01-August-2020 14:47:34</p>
              <p class="h6">08-November-2020 12:18:15</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import Tabs from "@/components/Tabs/Tabs.vue";
import TabPane from "@/components/Tabs/TabPane.vue";

import LearningTab from "./ProfileTabs/LearningTab";
import LearningSettingsTab, { LearnSets } from "./ProfileTabs/LearningSettingsTab";
import ClassificationSettingsTab from "./ProfileTabs/ClassificationSettingsTab";
import BlackWhiteListTab from "./ProfileTabs/BlackWhiteListTab";

import axios from "axios";

import {API_URL} from "../axios-api.js";

export default {
  data() {
    return {
      lastLearn: "",
      totalTime: "",
      VolumeInbox: "",
      VolumeSpam: "",
    };
  },

  components: {
    Tabs,
    TabPane,

    LearningTab,
    LearningSettingsTab,
    ClassificationSettingsTab,
    BlackWhiteListTab,
  },

  created() {
    axios({
      method: "GET",
      url: API_URL + "/profile/last_learn/",
      headers: {
        Authorization: `Token ${this.$store.state.accessToken}`,
      },
    })
      .then((response) => {
        this.lastLearn = response.data.lastLearn;
        this.totalTime = response.data.totalTime;
        this.VolumeInbox = response.data.VolumeInbox;

        this.VolumeSpam = response.data.VolumeSpam;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
<style></style>
