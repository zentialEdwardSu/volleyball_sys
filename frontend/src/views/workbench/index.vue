<template>
    <div class="workbench-main">
            <el-dialog v-model="dialoginputVisible" title="Input command">
                <span>Curent working dir: server_root</span>
  	            <el-input v-model="input" placeholder="Please input" clearable />
                <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialoginputVisible = false">Cancel</el-button>
                    <el-button type="primary" @click="sendcommand">Confirm</el-button>
                </span>
                </template>
            </el-dialog>
        <div class="workbench-main-left">
            <div class="Mainview">
                <el-image class="eimg" fit="scale-down" :src="states.streampos.Main">
                    <template #error>
                        <el-skeleton  throttle=500 loading=true animated>
                            <template #template>
                                <el-skeleton-item variant="image" style="height:100%"/>
                            </template>
                        </el-skeleton>
                    </template>
                </el-image>
            </div>
            <div class="info">
                <div>
                    <label>MainView : </label>
                    <label>原视频</label>
                    <el-button  v-text="slots.Main[0]" @click="conStreamMain" style="float:right; width:200px;" :type="slots.Main[1]"></el-button>
                    <el-button  style="float:right; width:200px;margin-right:20px;" type="success" color="#626aef" dark="isDark" @click="dialoginputVisible = true">openinput</el-button>
                </div>
                <div>
                    <label>SideView-1 : </label>
                    <label>检测结果视频</label>
                    <!-- <label v-text="frpsSide1"></label> -->
                    <el-button v-text="slots.SideUp[0]" @click="conStreamSide1" style="float:right; width:200px" :type="slots.SideUp[1]"></el-button>
                </div>
                <div>
                    <label>SideView-2 : </label>
                    <label>2D运动视频</label>
                    <!-- <label v-text="frpsSide2"></label> -->
                    <el-button v-text="slots.SideDown[0]" @click="conStreamSide2" style="float:right; width:200px" :type="slots.SideDown[1]"></el-button>
                </div>
            </div>
        </div>
        <div class="workbench-main-right">
            <div class="side1">
                <el-image fit="scale-down" class="eimg" :src="states.streampos.SideUp">
                <template #error>
                    <el-skeleton throttle=500  loading=true animated>
                        <template #template>
                            <el-skeleton-item variant="image" style="height:100%"/>
                        </template>
                    </el-skeleton>
                </template>
                </el-image>
            </div>
            <div style="height:10px"></div>
            <div class="side2">
                <el-image fit="scale-down" class="eimg" :src="states.streampos.SideDown">
                <template #error>
                    <el-skeleton throttle=500 loading=true animated>
                        <template #template>
                            <el-skeleton-item variant="image" style="height:100%"/>
                        </template>
                    </el-skeleton>
                </template>
                </el-image>
            </div>
        </div>
        <!-- <p>这里是workbench</p> -->
    </div>
</template>
<script setup>
import {ref,onMounted,h} from 'vue'
import axios from 'axios'
import store from '../../store/store.ts'
import { ElNotification } from 'element-plus'
// const pageSetting = ref(null);


const states = ref(store.states)
console.log(states.value)
const slots = ref({
    Main:[states.value.views.Main?'streaming':'Interupt',states.value.views.Main?'success':'danger'],
    SideUp:[states.value.views.SideUp?'streaming':'Interupt',states.value.views.SideUp?'success':'danger'],
    SideDown:[states.value.views.SideDown?'streaming':'Interupt',states.value.views.SideDown?'success':'danger'],
})
const dialoginputVisible = ref(false)
const input = ref("")


const conStreamMain=()=>{
    store.updateMainview(store.states.views.Main?false:true)
    slots.value.Main = [states.value.views.Main?'streaming':'Interupt',states.value.views.Main?'success':'danger']
    console.log("main",states.value.views.Main)
    console.log("main",slots.value.Main)

};
const conStreamSide1=()=>{
    store.updateSideUpview(store.states.views.SideUp?false:true)
    slots.value.SideUp = [states.value.views.SideUp?'streaming':'Interupt',states.value.views.SideUp?'success':'danger']
    console.log("sideup",states.value.views.SideUp)
    console.log("sideup",slots.value.SideUp)
};
const conStreamSide2=()=>{
    store.updateSideDownview(store.states.views.SideDown?false:true)
    slots.value.SideDown = [states.value.views.SideDown?'streaming':'Interupt',states.value.views.SideDown?'success':'danger']
    console.log("sidedown",states.value.views.SideDown)
    console.log("sidedown",slots.value.SideDown)
};
const ELok = () =>{
    ElNotification({
    title: 'OK',
    message: h('i', { style: 'color: teal' }, 'Command Process succeed'),
  })
}

const ELerr = (e) =>{
    ElNotification({
    title: 'WARN',
    message: h('i', { style: 'color: teal' }, 'something wrong happen '+e),
  })
}

const sendcommand = () =>{
    dialoginputVisible.value = false
    axios.post("http://127.0.0.1:5000/api/postcommand",{"body":input.value})
    .then(function(response){
        let res = response.data;
        console.log(res)
        console.log(res.error,res.errormsg)
        if(res.error){
            ELerr(res.errormsg)
        }else{
            ELok()
        }
        get_src();
        input.value = ''
    })
    .catch(function (error){
        ElNotification({
            title:'Server error',
            message: h('i',{style: 'color:red'},"something wrong with server\n"+error)
        })
        console.log('Error',error)
    })
}

const get_src = () =>{
    axios
        .post("http://127.0.0.1:5000/api/getsrc")
        .then(function (response){
            // let res = response.data.body;
            store.updateStreampos(response.data.body);
            console.log(store.states);
        })
        .catch(function (error) { // 请求失败处理
            console.log('Error',error);
            store.updateStreampos(["http://127.0.0.1:5000/nosignal","http://127.0.0.1:5000/nosignal","http://127.0.0.1:5000/nosignal"]);
            console.log(store.state);
        });
}
onMounted(
    get_src
);
</script>
<style>
.workbench-main {
    display: flex;
    justify-content: space-around;
}
.workbench-main-left, .workbench-main-right {
    float:left;
    display:flex;
    flex-direction: column;
    justify-content: flex-start;
    /* border: 1px #000 solid; */

    height: 100vh;
}
.workbench-main-left {
    width: calc(50% - 10px);
}
.workbench-main-right {
    width: calc(50% - 10px);
}
.side1, .side2 {
    width: 100%;
    height: 45%;
    /* border: 1px #000 solid; */
}
.info{
    width:100%;
    height:30%
}
.Mainview{
    width: 100%;
    height: 70%;
}
.eimg {
    width:100%;
    height:100%;
}
.info > div {
    width: calc(100% - 60px);
    margin: 10px;
    padding: 20px;
    /* border: 1px #000 solid; */
}
.el-skeleton{
    width: 100%;
    height: 100%;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>