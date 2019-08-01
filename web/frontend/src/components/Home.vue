<template>
  <div>
    <el-container>
      <el-header>HEADER</el-header>
      <el-main>
        <el-row>
          <el-col :span="12">
            <el-row>
              <div class="block">
                <el-card>
                  <el-checkbox
                    :indeterminate="isIndeterminate"
                    v-model="checkAll"
                    @change="handleCheckAllChange"
                  >全选</el-checkbox>
                  <el-checkbox-group v-model="checkedCats" @change="handleCheckedCatsChange">
                    <el-checkbox
                      v-for="(item, index) in categories"
                      :label="item"
                      :key="index"
                    >{{ item | formatCatName }}</el-checkbox>
                  </el-checkbox-group>
                </el-card>
              </div>
            </el-row>
            <el-row>
              <div>
                <el-timeline>
                  <el-timeline-item
                    v-for="(item, index) in dataList"
                    :key="index"
                    size="large"
                    type="primary"
                    class="timeline-item"
                  >
                    <el-card shadow="hover" body-style="{ padding: '0px' }">
                      <h4>{{ item.title }}</h4>
                      <p>{{ item.content }}</p>
                    </el-card>
                  </el-timeline-item>
                  <el-timeline-item>
                    <el-card shadow="hover" class="load-more">
                      <p>加载更多...</p>
                    </el-card>
                  </el-timeline-item>
                </el-timeline>
              </div>
            </el-row>
          </el-col>
        </el-row>
      </el-main>

      <el-footer></el-footer>
    </el-container>
  </div>
</template>

<script>
const catOptions = [
  '36kr', '21jingji', 'tmtpost'
]
const catDic = {
  '36kr': '36氪',
  '21jingji': '21经济',
  'tmtpost': '钛媒体',
}
export default {
  data() {
    return {
      checkAll: false,
      isIndeterminate: true,
      categories: catOptions,
      checkedCats: ['36kr', '21jingji', 'tmtpost'],
      dataList: [
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" },
        { title: "标题标题标题", content: "内容内容内容" }
      ],
    };
  },
  methods: {
    handleCheckAllChange(val) {
      this.checkedCats = val ? catOptions : [];
      this.isIndeterminate = false
      this.getNewsData()
    },
    handleCheckedCatsChange(value) {
      let checkedCount = value.length;
      this.checkAll = checkedCount === this.categories.length
      this.isIndeterminate =
        checkedCount > 0 && checkedCount < this.categories.length
      this.getNewsData()
    },
    getNewsData() {
      console.log(this.checkedCats)
      const path = this.$host + "/api/newsflow"
      this.$ajax.get(path, {
        params: {
          category: this.checkedCats
        },
        paramsSerializer: params => {
          return this.$qs.stringify(params, { indices: false })
        }
      })
      .then(res => {
        console.log(res)
        this.dataList = res.data
      })
    },
  },
  filters: {
    formatCatName(name) {
      let catName = catDic[name]
      return catName
    }
  }
};
</script>

<style lang="css">
.timeline-item {
  padding: 5px;
}

.load-more {
  height: 50px;
}
</style>

