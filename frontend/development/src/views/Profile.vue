<template>
    <div class="profile-page">

        <section class="section section-skew">
    <div class="row justify-content-center">
        <div class="col-lg-6">
            <!-- Tabs with icons -->
            <tabs fill class="flex-column flex-md-row">
                <card shadow slot-scope="{activeTabIndex}">
                    <tab-pane key="tab1">
                        <template slot="title">
                            <i class="ni ni-cloud-upload-96 mr-2"></i>Train
                        </template>
                        <LearningTab></LearningTab>
                    </tab-pane>

                    <tab-pane key="tab2">
                        <template slot="title">
                            <i class="ni ni-bell-55 mr-2"></i>Learning settings
                        </template>

                        <LearningSettingsTab></LearningSettingsTab>
                    </tab-pane>

                    <tab-pane key="tab3">
                        <template slot="title">
                            <i class="ni ni-calendar-grid-58 mr-2"></i>Classification settings
                        </template>

                        <ClassificationSettingsTab></ClassificationSettingsTab>
                    </tab-pane>

                    <tab-pane key="tab4">
                        <template slot="title">
                            <i class="ni ni-cloud-upload-96 mr-2"></i>White and Black lists
                        </template>
                        <BlackWhiteListTab></BlackWhiteListTab>
                    </tab-pane>
                </card>
            </tabs>
        </div>
        <div class="col-lg-4">
            <br>
            <h1 class="display-4">Statistics</h1>
            <div>
                <p class="h4">Current status</p>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Model file existance</p>
                </div>
                <div class='col-lg-4'>
                    <p >Present</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Action Idle:</p>
                </div>
                <div class='col-lg-4'>
                    <p >no action</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Prev. operation info</p>
                </div>
                <div class='col-lg-4'>
                    <p >OK</p>
                </div>
            </div>

            <div>
                <p class="h4">Totals</p>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">First train start</p>
                </div>
                <div class='col-lg-4'>
                    <p >01-August-2020 14:47:34</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Last train finish</p>
                </div>
                <div class='col-lg-4'>
                    <p >08-November-2020 12:18:22</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Total time</p>
                </div>
                <div class='col-lg-4'>
                    <p >00:00:13</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Messages downloaded total
                        in all trainups	Inbox:</p>
                </div>
                <div class='col-lg-4'>
                    <p>47</p>
                </div>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-4'>
                    <p class="h6">Spam:</p>
                </div>
                <div class='col-lg-4'>
                    <p>19</p>
                </div>
            </div>

            <div>
                <p class="h4">TrainUp's history</p>
            </div>
            <div class="row justify-content-left">
                <div class='col-lg-8'>
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
import LearningSettingsTab from "./ProfileTabs/LearningSettingsTab";
import ClassificationSettingsTab from "./ProfileTabs/ClassificationSettingsTab";
import BlackWhiteListTab from "./ProfileTabs/BlackWhiteListTab";


export default {
    components: {
        Tabs,
        TabPane,
        

        LearningTab,
        LearningSettingsTab,
        ClassificationSettingsTab,
        BlackWhiteListTab
    },

};
</script>
<style>
</style>
