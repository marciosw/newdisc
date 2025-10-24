import React from "react";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

// registra os módulos do Chart.js
ChartJS.register(
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Tooltip,
  Legend
);

export default function DynamicChart() {
  // --- Dados de exemplo (mockados) ---
  const data = {
    labels: ["D", "I", "S", "C"],
    datasets: [
      {
        label: "Lorem Ipsum",
        data: [120, 150, 180, 90, 200, 170, 210],
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        fill: true,
        tension: 0.3,
      },
      {
        label: "Lorem Ipsum",
        data: [100, 130, 160, 70, 150, 140, 180],
        borderColor: "rgba(255, 99, 132, 1)",
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        fill: true,
        tension: 0.3,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: true },
      title: { display: true, text: "(Exemplo Estático)" },
    },
    scales: {
      y: { beginAtZero: true },
    },
  };

  return (
    <div style={{ width: "300px", margin: "auto" }}>
      <Line data={data} options={options} />
    </div>
  );
}
