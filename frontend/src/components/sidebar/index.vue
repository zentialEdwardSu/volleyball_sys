<template>
<!--    导航栏的顶部-->
  <!-- <el-affix class="el-affix-Cursor" :z-index="1200" style="" @click="gotoHome">
    <span>DisplayPanel</span>
  </el-affix> -->
  <el-menu
    class="el-menu-vertical-demo"
    :default-active="activepart"
    :collapse="isCollapse"
    @mouseover="unflod"
    @mouseout="flod"
    router>
    <el-menu-item index="1" @click="gotoWorkbench">
      <el-icon><icon-menu /></el-icon>
      <template #title>Workbench</template>
    </el-menu-item>
    <el-menu-item index="2" @click="gotoSetting">
      <el-icon><setting /></el-icon>
      <template #title>Prompt</template>
    </el-menu-item>
    <el-menu-item index="3" style="bottom:0;position:fixed" @click="gotoAbout">
      <el-icon><collection/></el-icon>
      <template #title>About</template>
    </el-menu-item>
  </el-menu>
</template>

<script setup>
    import {ref,reactive,onMounted,defineEmits,defineExpose} from 'vue'
    import {
      Setting,
      Collection,
      Menu as IconMenu,
    }from '@element-plus/icons-vue'
    import {useRouter,useRoute} from 'vue-router'
    const isCollapse=ref(true);
    const test=ref(123456)
    // console.log("子组件")
    // console.log(isCollapse)
    const activepart=ref("1")
    const routers = useRouter();
    const emits=defineEmits(["collachange"])
    // provide("isCollapse",isCollapse)
    const gotoHome = () => {
        routers.push({
            path:'/w/workbench'
        });
    
    };
    const gotoWorkbench = () =>{
        activepart.value="1"
        routers.push({
            path:'/w/workbench'
        });
    };
    const gotoSetting = () =>{
        activepart.value="2"
        routers.push({
            path:"/w/setting"
        });
    };
    const gotoPrompt = () =>{

    }
    const gotoAbout = () =>{
        activepart.value="3"
        routers.push({
            path:"/w/about"
        });
    };
    const flod = ()=>{
      // emits('collachange', isCollapse.value);
      setTimeout(()=>{
          isCollapse.value=true
          emits('collachange', '60px');
          console.log("mouse out of area")
      } ,"50")
      // isCollapse.value=true
      // console.log("mouse in area")
    }
    const unflod = ()=>{
      // $emit('change-aside', '200px');
      // provide("colla",isCollapse)
      // emits('collachange', isCollapse.value);
      setTimeout(()=>{
        isCollapse.value=false;
        emits('collachange', '200px');
        console.log("mouse in area")
      },"50")
    }
    defineExpose({
      isCollapse,
      test
    })
    onMounted(() => {
        },
    );
</script>
<style>
.basement{
    position: fixed;
    width: 200px;
    bottom: 0;
  }
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 100%;
}

</style>
