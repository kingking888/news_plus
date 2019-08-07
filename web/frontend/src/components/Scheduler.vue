<template>
  <el-row>
    <el-table :data="tableData">
      <el-table-column prop="name" label="爬虫" width="180"></el-table-column>
      <el-table-column prop="status" label="状态" width="180"></el-table-column>
      <el-table-column label="操作" width="180">
        <template slot-scope="scope">
          <el-button @click="clickStart(scope.row.name)" type="text" size="small">开始</el-button>
          <el-button @click="clickPause(scope.row.name)" type="text" size="small">暂停</el-button>
          <el-button @click="clickResume(scope.row.name)" type="text" size="small">继续</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          name: "bloomberg",
          status: "off",
        },
        
      ]
    };
  },
  created() {

  },
  methods: {
    spiderSched(spider, action) {
      const url = this.$host + "/api/scheduler"
      this.$ajax
        .get(url, {
          params: {
            spider: spider,
            action: action
          },
          paramsSerializer: params => {
            return this.$qs.stringify(params, { indices: false });
          }
        })
        .then(res => {
          console.log(res)
        })
    },
    clickStart(name) {
      console.log(name)
      let spider = 'run_' + name
      let action = 'start'
      this.spiderSched(spider, action)
    },
    clickPause(name) {
      console.log(name)
      let spider = 'run_' + name
      let action = 'pause'
      this.spiderSched(spider, action)
    },
    clickResume(name) {
      console.log(name)
      let spider = 'run_' + name
      let action = 'resume'
      this.spiderSched(spider, action)
    },
  }
};
</script>

<style>
</style>

