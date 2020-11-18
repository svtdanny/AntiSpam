<template>
    <div class="row">
    <div class="col">
        <div class="row">
                <p class='h4'>Delete</p>
        </div>
        <div class="row">
            <base-input class="w-75" placeholder="email(s) separated by commas">
            </base-input>      
        </div>
        <div class="row"> 
            <base-button type="primary" size=sm>Delete</base-button>
        </div>
        <br>

        <div class="row">
            <p class='h4'>Add</p>
        </div>
        <div class="row">
                <base-input class="w-75" placeholder="email(s) separated by commas">
                </base-input>      
        </div>
        <div class="row"> 
            <base-button type="primary" size=sm>Add to White</base-button>
            <base-button type="primary" size=sm>Add to Black</base-button>
        </div>
        <br>

        <div class="row">
            <p class='h4'>Add from file</p>
        </div>
        <div class="row">
                <input type="file">
        </div>
        <br>
        <div class="row">
                <base-dropdown >
                    <base-button slot="title" type="secondary" class="dropdown-toggle">
                    List
                    </base-button>
                    <a class="dropdown-item" href="#">White</a>
                    <a class="dropdown-item" href="#">Black</a>
                </base-dropdown>   

            <base-button type="primary" size=sm>Add</base-button>
        </div>

    </div>
    
    <div class="col">
        <div class="row">
            <p class='h4'>White list</p>
        </div>

        <div class="row">
            <ul class="list-unstyled">
                <li class="row-sm-3">aaa@test.ru</li>
                <li class="row-sm-3">b@testing.com</li>
                <li class="row-sm-3">aaacccbbb@test.ru</li>
            </ul>
        </div>

        <div class="row mt-3">
            <p class='h4'>Black list</p>
        </div>

        <div class="row">
            <ul class="list-unstyled">
                <li class="row-sm-3">BadPerson@test.ru</li>
                <li class="row-sm-3">mail@onlineshop.com</li>
                <li class="row-sm-3">spammer@mail.ru</li>
            </ul>
        </div>
    </div>
    </div>

    
</template>

<script>
import BaseDropdown from "@/components/BaseDropdown.vue";

export default {
    components: {
        BaseDropdown,
    },

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