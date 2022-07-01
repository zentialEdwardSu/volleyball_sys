const store = {
    states:{
        "streampos":{
            "Main":"",
            "SideUp":"",
            "SideDown":""
        },
        "views":{
            "Main":true,
            "SideUp":true,
            "SideDown":true
        },
        "ready":false,
        "openDialog":false,
    },
    updateStreampos(data:Array<string>){
        this.states.streampos.Main = data[0]
        this.states.streampos.SideUp = data[1]
        this.states.streampos.SideDown = data[2]

        console.log("[Update] Streampos:",data);
    },
    updateMainview(st:boolean){
        this.states.views.Main = st
    },
    updateSideUpview(st:boolean){
        this.states.views.SideUp = st
    },
    updateSideDownview(st:boolean){
        this.states.views.SideDown = st
    },
    isReady(st:boolean){
        this.states.ready = st
    }
}
export default store