webpackJsonp([1],{"/7TP":function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("7+uW"),s={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var r=n("VU/8")({name:"App"},s,!1,function(t){n("/7TP")},null,null).exports,i=n("/ocq");function o(t){return("00"+t).substr(t.length)}var c=["36kr","21jingji","tmtpost","doit","zhitongcaijing","bloomberg"],l={"36kr":"36氪","21jingji":"21经济",tmtpost:"钛媒体",doit:"DOIT",zhitongcaijing:"智通财经",bloomberg:"bloomberg"},u={data:function(){return{checkAll:!1,isIndeterminate:!0,categories:c,checkedCats:["36kr","21jingji","tmtpost","doit","zhitongcaijing"],dataList:[]}},created:function(){this.getNewsData()},methods:{handleCheckAllChange:function(t){this.checkedCats=t?c:[],this.isIndeterminate=!1,this.getNewsData()},handleCheckedCatsChange:function(t){var e=t.length;this.checkAll=e===this.categories.length,this.isIndeterminate=e>0&&e<this.categories.length,this.getNewsData()},getNewsData:function(){var t=this;console.log(this.checkedCats);var e=this.$host+"/api/newsflow";this.$ajax.get(e,{params:{category:this.checkedCats,skip:0},paramsSerializer:function(e){return t.$qs.stringify(e,{indices:!1})}}).then(function(e){console.log(e),t.dataList=e.data})},getMoreData:function(){var t=this,e=this.dataList.length;console.log(e);var n=this.$host+"/api/newsflow";this.$ajax.get(n,{params:{category:this.checkedCats,skip:e},paramsSerializer:function(e){return t.$qs.stringify(e,{indices:!1})}}).then(function(e){var n=t.dataList.concat(e.data);t.dataList=n})},ifTag:function(t){return!!t&&0!=t.length}},filters:{formatCatName:function(t){return l[t]},formatTS:function(t){return function(t,e){/(y+)/.test(e)&&(e=e.replace(RegExp.$1,(t.getFullYear()+"").substr(4-RegExp.$1.length)));var n={"M+":t.getMonth()+1,"d+":t.getDate(),"h+":t.getHours(),"m+":t.getMinutes(),"s+":t.getSeconds()};for(var a in n)if(new RegExp("("+a+")").test(e)){var s=n[a]+"";e=e.replace(RegExp.$1,1===RegExp.$1.length?s:o(s))}return e}(new Date(1e3*t),"yyyy/MM/dd hh:mm")}}},h={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("el-container",[n("el-header",[n("h1",[t._v("PLUS+ 新闻采集")])]),t._v(" "),n("el-main",[n("el-row",[n("el-col",{attrs:{span:8}},[n("el-row",[n("div",{staticClass:"block"},[n("el-card",[n("el-checkbox",{attrs:{indeterminate:t.isIndeterminate},on:{change:t.handleCheckAllChange},model:{value:t.checkAll,callback:function(e){t.checkAll=e},expression:"checkAll"}},[t._v("全选")]),t._v(" "),n("el-checkbox-group",{on:{change:t.handleCheckedCatsChange},model:{value:t.checkedCats,callback:function(e){t.checkedCats=e},expression:"checkedCats"}},t._l(t.categories,function(e,a){return n("el-checkbox",{key:a,attrs:{label:e}},[t._v(t._s(t._f("formatCatName")(e)))])}),1)],1)],1)]),t._v(" "),n("el-row",[n("div",[t._l(t.dataList,function(e,a){return n("el-card",{key:a,staticClass:"news-card",attrs:{shadow:"hover","body-style":"{ padding: '0px' }"}},[n("h4",{staticClass:"title"},[n("a",{attrs:{href:e.href,target:"_blank"}},[t._v(t._s(e.title))])]),t._v(" "),n("div",{staticClass:"info"},[n("span",{staticClass:"source"},[t._v(t._s(t._f("formatTS")(e.ts_crawl)))]),t._v(" "),n("span",[t._v("信息来源: "+t._s(t._f("formatCatName")(e.source)))])]),t._v(" "),n("p",{staticClass:"summary"},[t._v(t._s(e.content))]),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:t.ifTag(e.tags),expression:"ifTag(item.tags)"}],staticClass:"tag"},[n("i",{staticClass:"iconfont icon-tag"}),t._v(" "),t._l(e.tags,function(e,a){return n("a",{key:a,attrs:{href:e.tag_href,target:"_blank"}},[t._v(t._s(e.tag))])})],2)])}),t._v(" "),n("el-card",{staticClass:"load-more",attrs:{shadow:"hover"}},[n("p",{on:{click:function(e){return t.getMoreData()}}},[t._v("加载更多...")])])],2)])],1)],1)],1),t._v(" "),n("el-footer")],1)],1)},staticRenderFns:[]};var d=n("VU/8")(u,h,!1,function(t){n("R/3J")},null,null).exports,f={data:function(){return{tableData:[{name:"bloomberg",status:"off"}]}},created:function(){},methods:{spiderSched:function(t,e){var n=this,a=this.$host+"/api/scheduler";this.$ajax.get(a,{params:{spider:t,action:e},paramsSerializer:function(t){return n.$qs.stringify(t,{indices:!1})}}).then(function(t){console.log(t)})},clickStart:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"start")},clickPause:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"pause")},clickResume:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"resume")}}},p={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-row",[n("el-table",{attrs:{data:t.tableData}},[n("el-table-column",{attrs:{prop:"name",label:"爬虫",width:"180"}}),t._v(" "),n("el-table-column",{attrs:{prop:"status",label:"状态",width:"180"}}),t._v(" "),n("el-table-column",{attrs:{label:"操作",width:"180"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){return t.clickStart(e.row.name)}}},[t._v("开始")]),t._v(" "),n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){return t.clickPause(e.row.name)}}},[t._v("暂停")]),t._v(" "),n("el-button",{attrs:{type:"text",size:"small"},on:{click:function(n){return t.clickResume(e.row.name)}}},[t._v("继续")])]}}])})],1)],1)},staticRenderFns:[]};var g=n("VU/8")(f,p,!1,function(t){n("aUOD")},null,null).exports,m={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("About")])])}]},v=n("VU/8")(null,m,!1,null,null,null).exports,_={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("404 - NotFound")])])}]},k=n("VU/8")(null,_,!1,null,null,null).exports;a.default.use(i.a);var b=new i.a({mode:"history",routes:[{path:"/",name:"Home",component:d},{path:"/scheduler",name:"Scheduler",component:g},{path:"/about",name:"About",component:v},{path:"*",name:"NotFound",component:k}]}),w=n("mtWM"),C=n.n(w),y=n("mw3O"),x=n.n(y),$=n("zL8q"),R=n.n($);n("tvR6"),n("OMRB");a.default.config.productionTip=!1,a.default.use(R.a),a.default.prototype.$ajax=C.a,a.default.prototype.$qs=x.a,a.default.prototype.$host="http://139.196.102.128:8000",new a.default({el:"#app",router:b,components:{App:r},template:"<App/>"})},OMRB:function(t,e){},"R/3J":function(t,e){},aUOD:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.4149e7b499c137daed7b.js.map