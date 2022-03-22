<script>
import { Bar } from "vue-chartjs";
import Axios from "axios";

export default {
  name: "WeeklyTab",
  extends: Bar,
  mounted() {
    this.fetchWeeklyReport();

    var ctx = document.getElementById("#bar-chart");
    ctx.height = 300;
  },
  methods: {
    fetchWeeklyReport() {
      Axios.get(this.$hostname + "/weekly-income", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          for (let i = resp.data.report.length - 2; i >= 0; i--) {
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
          "شنبه",
          "یکشنبه",
          "دوشنبه",
          "سه شنبه",
          "چهارشنبه",
          "پنجشنبه",
          "جمعه",
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
          labels: {
            fontColor: "black",
            defaultFontFamily: "IRANsans",
          },
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
