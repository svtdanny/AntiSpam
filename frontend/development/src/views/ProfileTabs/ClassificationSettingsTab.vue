<template>
    <div class='col'>
    <div class="row mt-3">
    <p class='h6'>Define custom ISD spam filter strength</p>
    </div>
        
    <base-radio name="radio0" class="mb-3" v-model="radio.radio1">
         Lenient (-0.4)
    </base-radio>

    <base-radio name="radio1" class="mb-3" v-model="radio.radio2">
 	    Moderate (-0.2)
    </base-radio>

    <base-radio name="radio2" class="mb-3" v-model="radio.radio1">
 	    Submoderate (-0.1)
    </base-radio>

    <base-radio name="radio3" class="mb-3" v-model="radio.radio1">
 	    Normal (0.0)
    </base-radio>

    <base-radio name="radio4" class="mb-3" v-model="radio.radio1">
 	    Subaggressive (0.1)
    </base-radio>

    <base-radio name="radio5" class="mb-3" v-model="radio.radio1">
 	    Agressive (0.2)
    </base-radio>

    <base-radio name="radio6" class="mb-3" v-model="radio.radio1">
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
        <base-button type="primary" class="my-3" size=sm>Save</base-button>
        <base-button tag="a" href="#/" type="secondary" class="my-3" size=sm>Close</base-button>
    </div>
    </div>
</template>

<script>
export default {
    data() {
    return {
        checkboxes: {
            unchecked: false,
            checked: true,
            uncheckedDisabled: false,
            checkedDisabled: true
        },
        radio: {
            radio1: "radio3",
        },
        }
}

};
</script>
<style>
</style>
