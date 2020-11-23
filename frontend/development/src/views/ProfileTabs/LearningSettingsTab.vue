<template>
    <div class="col">
    <div class="row mt-3">
        
            <p class='h6'>Use predifined model:</p>

            <base-checkbox v-model="checkboxes.checked">
            <p></p>
            </base-checkbox>
    </div>
    <div class="row">
            <p class='h6'>Train max volume Inbox:</p>
    </div>
    <div class="row">
            <base-input placeholder="1..2000">
            </base-input>      
    </div>

    <div class="row">
            <p class='h6'>Train max volume Spam:</p>
    </div>
    <div class="row">
            <base-input placeholder="1..2000">
            </base-input>      
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
    }
}

};


</script>
<style>
</style>
