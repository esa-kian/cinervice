<script>
import Axios from "axios";
import { Bar } from "vue-chartjs";

export default {
  name: "CurrentTab",
  extends: Bar,
  mounted() {
    this.fetchWeeklyReport();

    var ctx = document.getElementById("#bar-chart");
    ctx.height = 300;
  },
  methods: {
    fetchWeeklyReport() {
      Axios.get(this.$hostname + "/yearly-income", {
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
          "فروردین",
          "اردیبهشت",
          "خرداد",
          "تیر",
          "مرداد",
          "شهریور",
          "مهر",
          "آبان",
          "آذر",
          "دی",
          "بهمن",
          "اسفند",
        ],
        datasets: [
          {
            label: "درآمد",
            backgroundColor: "rgba(238, 248, 239,1)",
            borderColor: "rgba(122, 179, 131, 1)",
            borderWidth: 1,
            data: [100, 200, 130, 5000, 300, 1200, 30, 200, 500],
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
