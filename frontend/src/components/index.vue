<template>
    <el-container class="mainlayout"
    style="height: 1000px;"
    >
        <el-container>
            <el-header class="page-header">
                    <el-progress 
                    :percentage="100" 
                    :indeterminate="isdeterminate" 
                    :duration="2" 
                    :show-text="false" 
                    color="#1f627c"/>
            </el-header>
            <el-container>
                <el-aside id="sidebar">
                    <Sidebar @collachange="changeAside"></Sidebar>
                </el-aside>
                <el-main>
                    <Menus></Menus>
                </el-main>
            </el-container>
        </el-container>
    </el-container>
</template>
<script setup lang="ts">
import Sidebar from "./sidebar/index.vue"
import Menus from "./menu/index.vue"
import {ref} from "vue"

var fatherCollaspe;
const isdeterminate= ref(true);
const stop_determinate=()=>{
    isdeterminate.value=false;
}
const strt_determinate=()=>{
    isdeterminate.value=true;
}
// const changeColla=(data)=>{
//     fatherCollaspe = data;
//     console.log("Father->"+fatherCollaspe)
// }
const changeAside = (data:string) => {
    console.log(data);
    let asideWidth= document.getElementById("sidebar");
    asideWidth.style.width=data;
    console.log("Now width "+asideWidth.width)
}
</script>
<style scoped>
* {
    margin:0;
    padding:0;
}
.mainlayout .el-progress{
    width: 100%;
}
.el-menu{
  border-right-width: 0;
}
 .el-main{
    margin: 0;
}
.mainlayout .el-aside {
    width: 60px;
    transition: 0.5s;
    color: var(--el-text-color-primary);
    background: #fff !important;
    border-right: solid 1px #cacaca;
    box-sizing: border-box;
    margin:10px;
}
.page-header{
    height:25px;
}
</style>