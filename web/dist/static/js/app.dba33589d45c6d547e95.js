webpackJsonp([1],{"/7TP":function(t,e){},NHnr:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("7+uW"),s={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var i=a("VU/8")({name:"App"},s,!1,function(t){a("/7TP")},null,null).exports,r=a("/ocq");function o(t){return("00"+t).substr(t.length)}var l=["36kr","21jingji","tmtpost","doit","zhitongcaijing","thepaper","kankan","yicai","bloomberg"],c={"36kr":"36氪","21jingji":"21经济",tmtpost:"钛媒体",doit:"DOIT",zhitongcaijing:"智通财经",thepaper:"澎湃",kankan:"看看新闻",yicai:"第一财经",bloomberg:"bloomberg"},u={data:function(){return{checkAll:!1,isIndeterminate:!0,categories:l,checkedCats:["36kr","21jingji","tmtpost","doit","zhitongcaijing","thepaper","kankan","yicai"],dataList:[],loading:!1}},created:function(){this.getNewsData()},methods:{handleCheckAllChange:function(t){this.checkedCats=t?l:[],this.isIndeterminate=!1,this.getNewsData()},handleCheckedCatsChange:function(t){var e=t.length;this.checkAll=e===this.categories.length,this.isIndeterminate=e>0&&e<this.categories.length,this.getNewsData()},getNewsData:function(){var t=this;console.log(this.checkedCats);var e=this.$host+"/api/newsflow";this.$ajax.get(e,{params:{category:this.checkedCats,skip:0},paramsSerializer:function(e){return t.$qs.stringify(e,{indices:!1})}}).then(function(e){console.log(e),t.dataList=e.data})},getMoreData:function(){var t=this;this.loading=!0;var e=this.dataList.length,a=this.$host+"/api/newsflow";this.$ajax.get(a,{params:{category:this.checkedCats,skip:e},paramsSerializer:function(e){return t.$qs.stringify(e,{indices:!1})}}).then(function(e){var a=t.dataList.concat(e.data);t.dataList=a,t.loading=!1})},ifTag:function(t){return!!t&&0!=t.length}},filters:{formatCatName:function(t){return c[t]},formatTS:function(t){return function(t,e){/(y+)/.test(e)&&(e=e.replace(RegExp.$1,(t.getFullYear()+"").substr(4-RegExp.$1.length)));var a={"M+":t.getMonth()+1,"d+":t.getDate(),"h+":t.getHours(),"m+":t.getMinutes(),"s+":t.getSeconds()};for(var n in a)if(new RegExp("("+n+")").test(e)){var s=a[n]+"";e=e.replace(RegExp.$1,1===RegExp.$1.length?s:o(s))}return e}(new Date(1e3*t),"yyyy/MM/dd hh:mm")}}},h={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("el-container",[a("el-header",[a("h1",[t._v("PLUS+ 新闻采集")])]),t._v(" "),a("el-main",[a("el-row",{attrs:{gutter:10}},[a("el-col",{attrs:{span:8}},[a("el-row",[a("div",{staticClass:"block"},[a("el-collapse",[a("el-collapse-item",{attrs:{title:"筛选"}},[a("div",{staticClass:"filter-block"},[a("el-checkbox",{attrs:{indeterminate:t.isIndeterminate},on:{change:t.handleCheckAllChange},model:{value:t.checkAll,callback:function(e){t.checkAll=e},expression:"checkAll"}},[t._v("全选")]),t._v(" "),a("el-checkbox-group",{on:{change:t.handleCheckedCatsChange},model:{value:t.checkedCats,callback:function(e){t.checkedCats=e},expression:"checkedCats"}},t._l(t.categories,function(e,n){return a("el-checkbox",{key:n,attrs:{label:e}},[t._v(t._s(t._f("formatCatName")(e)))])}),1)],1)])],1)],1)]),t._v(" "),a("el-row",[a("div",[t._l(t.dataList,function(e,n){return a("el-card",{key:n,staticClass:"news-card",attrs:{shadow:"hover","body-style":"{ padding: '0px' }"}},[a("h4",{staticClass:"title"},[a("a",{attrs:{href:e.href,target:"_blank"}},[t._v(t._s(e.title))])]),t._v(" "),a("div",{staticClass:"info"},[a("span",{staticClass:"source"},[t._v(t._s(t._f("formatTS")(e.ts_crawl)))]),t._v(" "),a("span",[t._v("信息来源: "+t._s(t._f("formatCatName")(e.source)))])]),t._v(" "),a("p",{staticClass:"summary"},[t._v(t._s(e.content))]),t._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:t.ifTag(e.tags),expression:"ifTag(item.tags)"}],staticClass:"tag"},[a("i",{staticClass:"iconfont icon-tag"}),t._v(" "),t._l(e.tags,function(e,n){return a("a",{key:n,attrs:{href:e.tag_href,target:"_blank"}},[t._v(t._s(e.tag))])})],2)])}),t._v(" "),a("el-card",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],staticClass:"load-more",attrs:{shadow:"hover"}},[a("el-button",{attrs:{type:"text"},on:{click:function(e){return t.getMoreData()}}},[t._v("加载更多")])],1)],2)])],1)],1)],1),t._v(" "),a("el-footer")],1)],1)},staticRenderFns:[]};var d=a("VU/8")(u,h,!1,function(t){a("Ohu2")},null,null).exports,f={data:function(){return{tableData:[{name:"bloomberg",status:"off"}]}},created:function(){},methods:{spiderSched:function(t,e){var a=this,n=this.$host+"/api/scheduler";this.$ajax.get(n,{params:{spider:t,action:e},paramsSerializer:function(t){return a.$qs.stringify(t,{indices:!1})}}).then(function(t){console.log(t)})},clickStart:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"start")},clickPause:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"pause")},clickResume:function(t){console.log(t);var e="run_"+t;this.spiderSched(e,"resume")}}},p={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-row",[a("el-table",{attrs:{data:t.tableData}},[a("el-table-column",{attrs:{prop:"name",label:"爬虫",width:"180"}}),t._v(" "),a("el-table-column",{attrs:{prop:"status",label:"状态",width:"180"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作",width:"180"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){return t.clickStart(e.row.name)}}},[t._v("开始")]),t._v(" "),a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){return t.clickPause(e.row.name)}}},[t._v("暂停")]),t._v(" "),a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){return t.clickResume(e.row.name)}}},[t._v("继续")])]}}])})],1)],1)},staticRenderFns:[]};var g=a("VU/8")(f,p,!1,function(t){a("aUOD")},null,null).exports,m={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("About")])])}]},v=a("VU/8")(null,m,!1,null,null,null).exports,_={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("404 - NotFound")])])}]},k=a("VU/8")(null,_,!1,null,null,null).exports;n.default.use(r.a);var b=new r.a({mode:"history",routes:[{path:"/",name:"Home",component:d},{path:"/scheduler",name:"Scheduler",component:g},{path:"/about",name:"About",component:v},{path:"*",name:"NotFound",component:k}]}),w=a("mtWM"),C=a.n(w),y=a("mw3O"),x=a.n(y),$=a("zL8q"),R=a.n($);a("tvR6"),a("OMRB");n.default.config.productionTip=!1,n.default.use(R.a),n.default.prototype.$ajax=C.a,n.default.prototype.$qs=x.a,n.default.prototype.$host="http://139.196.102.128:8000",new n.default({el:"#app",router:b,components:{App:i},template:"<App/>"})},OMRB:function(t,e){},Ohu2:function(t,e){},aUOD:function(t,e){},tvR6:function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.dba33589d45c6d547e95.js.map