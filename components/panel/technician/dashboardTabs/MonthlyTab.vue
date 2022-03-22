<script>
import { Bar } from "vue-chartjs";
import Axios from "axios";

export default {
  name: "MonthlyTab",
  extends: Bar,
  mounted() {
    this.fetchMonthlyReport();
    var ctx = document.getElementById("#bar-chart");
    ctx.height = 300;
  },
  methods: {
    fetchMonthlyReport() {
      Axios.get(this.$hostname + "/monthly-income", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          for (let i = resp.data.report.length-1; i >= 0; i--) {
            this.chartdata.datasets[0].data.push(eval(resp.data.report[i]));
          }
          this.renderChart(this.chartdata, this.options);
        })
        .catch((err) => {
          console.log(err, "can not data");
        });
    },
  },
  data() {
    return {
      chartdata: {
        labels: [
          "۱",
          "۲",
          "۳",
          "۴",
          "۵",
          "۶",
          "۷",
          "۸",
          "۹",
          "۱۰",
          "۱۱",
          "۱۲",
          "۱۳",
          "۱۴",
          "۱۵",
          "۱۶",
          "۱۷",
          "۱۸",
          "۱۹",
          "۲۰",
          "۲۱",
          "۲۲",
          "۲۳",
          "۲۴",
          "۲۵",
          "۲۶",
          "۲۷",
          "۲۸",
          "۲۹",
          "۳۰",
          "۳۱",
        ],
        datasets: [
          {
            label: "درآمد",
            backgroundColor: "rgba(238, 248, 239,1)",
            borderColor: "rgba(122, 179, 131, 1)",
            borderWidth: 1,
            data: [],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
        scales: {
          xAxes: [
            {
              gridLines: {
                color: "rgba(0, 0, 0, 0.05)",
              },
            },
          ],
          yAxes: [
            {
              ticks: {
                callback: function (value, index, values) {
                  return value + " تومان ";
                },
              },
              gridLines: {
                color: "rgba(0, 0, 0, 0.05)",
              },
            },
          ],
        },
      },
    };
  },
};
</script>

<style scoped>
canvas {
  height: 300px;
}
</style>
