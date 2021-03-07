<template>
<div id="wrapper">

    <LeftSideMenu />

    <div id="page-wrapper" class="gray-bg">

        <TopHeader />

        <nuxt />

        <BottomFooter />

    </div>
</div>
</template>

<style>

</style>

<script>

    import TopHeader from '~/components/TopHeader.vue'
    import LeftSideMenu from '~/components/LeftSideMenu.vue'
    import BottomFooter from '~/components/BottomFooter.vue'

    export default{
        components:{
            TopHeader,
            LeftSideMenu,
            BottomFooter
        },
        mounted(){
            this.$inspiniaInjectFunction();
        }

    }

</script>
