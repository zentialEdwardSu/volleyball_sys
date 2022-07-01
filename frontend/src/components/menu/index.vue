<template>
    <div>
        <router-view></router-view>
    </div>
</template>

<script>
    import {reactive, onMounted, toRefs} from 'vue'
    export default {
        setup() {
            const data = reactive({});
            onMounted(() => {

            });
            return {
                ...toRefs(data)
            }
        }
    }
</script>
