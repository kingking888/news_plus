<template>
  <div>
    <el-container>
      <el-header>
        <h1>PLUS+ 新闻采集</h1>
      </el-header>
      <el-main>
        <el-row>
          <el-col :span="8">
            <el-row>
              <!-- 筛选框 -->
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
                <!-- 新闻内容 -->
                <el-card
                  shadow="hover"
                  body-style="{ padding: '0px' }"
                  v-for="(item, index) in dataList"
                  :key="index"
                  class="news-card"
                >
                  <h4 class="title">
                    <a :href="item.href" target="_blank">{{ item.title }}</a>
                  </h4>
                  <div class="info">
                    <span class="source">{{ item.ts_crawl | formatTS }}</span>
                    <span>信息来源: {{ item.source | formatCatName }}</span>
                  </div>
                  <p class="summary">{{ item.content }}</p>
                  <div class="tag" v-show="ifTag(item.tags)">
                    <i class="iconfont icon-tag"></i>
                    <a :href="itm.tag_href" v-for="(itm, idx) in item.tags" :key="idx" target="_blank">{{ itm.tag }}</a>
                  </div>
                </el-card>
                <!-- 加载更多按钮 -->
                <el-card shadow="hover" class="load-more">
                  <p @click="getMoreData()">加载更多...</p>
                </el-card>
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
import { formatDate } from "@/common/date.js";
const catOptions = ["36kr", "21jingji", "tmtpost", "doit", "zhitongcaijing", "bloomberg"];
const catDic = {
  "36kr": "36氪",
  "21jingji": "21经济",
  "tmtpost": "钛媒体",
  "doit": "DOIT",
  "zhitongcaijing": "智通财经",
  "bloomberg": "bloomberg",
};
export default {
  data() {
    return {
      checkAll: false,
      isIndeterminate: true,
      categories: catOptions,
      checkedCats: ["36kr", "21jingji", "tmtpost", "doit", "zhitongcaijing"],
      dataList: []
    };
  },
  created() {
    this.getNewsData();
  },
  methods: {
    handleCheckAllChange(val) {
      this.checkedCats = val ? catOptions : [];
      this.isIndeterminate = false;
      this.getNewsData();
    },
    handleCheckedCatsChange(value) {
      let checkedCount = value.length;
      this.checkAll = checkedCount === this.categories.length;
      this.isIndeterminate =
        checkedCount > 0 && checkedCount < this.categories.length;
      this.getNewsData();
    },
    getNewsData() {
      console.log(this.checkedCats);
      const path = this.$host + "/api/newsflow";
      this.$ajax
        .get(path, {
          params: {
            category: this.checkedCats,
            skip: 0
          },
          paramsSerializer: params => {
            return this.$qs.stringify(params, { indices: false });
          }
        })
        .then(res => {
          console.log(res);
          this.dataList = res.data;
        });
    },
    getMoreData() {
      let skip = this.dataList.length;
      console.log(skip);
      const url = this.$host + "/api/newsflow";
      this.$ajax
        .get(url, {
          params: {
            category: this.checkedCats,
            skip: skip
          },
          paramsSerializer: params => {
            return this.$qs.stringify(params, { indices: false });
          }
        })
        .then(res => {
          let newList = this.dataList.concat(res.data);
          this.dataList = newList;
        });
    },
    // 判断tag是否存在
    ifTag(tag) {
      if (!tag) {
        return false
      }
      if (tag.length==0) {
        return false
      } else {
        return true
      }
    }
  },
  filters: {
    formatCatName(name) {
      let catName = catDic[name];
      return catName;
    },
    formatTS(timestamp) {
      let date = new Date(timestamp * 1000);
      return formatDate(date, "yyyy/MM/dd hh:mm");
    }
  }
};
</script>

<style lang="css">
.load-more {
  height: 50px;
}
.news-card {
  margin: 10px 0;
}
.title a{
  text-decoration: none;
  color: #262626;
}
.info {
  display: block;
  height: 20px;
  line-height: 20px;
  margin: 6px 0 10px;
  font-size: 12px;
  color: #a7a7a7;
}
.source {
  margin-right: 10px;
}
.summary {
  font-size: 14px;
  line-height: 24px;
  color: #787878;
  text-align: left;
}
.tag {
  font-size: 12px;
  text-align: left;
}
.tag a {
  text-decoration: none;
  margin: 0 5px;
  color: #409EFF;
}
</style>

