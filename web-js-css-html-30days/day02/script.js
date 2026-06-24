const app = document.querySelector("#app");
const state = {
  day: 2,
  title: "计数器",
  concept: "按钮事件和 DOM 更新",
  items: ["阅读代码", "修改样式", "观察交互"]
};

function render() {
  const list = state.items.map((item, index) => `<li>${index + 1}. ${item}</li>`).join("");
  app.innerHTML = `
    <section class="hero">
      <span>Day ${String(state.day).padStart(2, "0")}</span>
      <h1>${state.title}</h1>
      <p>${state.concept}</p>
      <button id="actionButton">完成一个练习步骤</button>
    </section>
    <section class="panel">
      <h2>今日清单</h2>
      <ul>${list}</ul>
    </section>
  `;

  document.querySelector("#actionButton").addEventListener("click", () => {
    state.items.push(`新步骤 ${state.items.length + 1}`);
    render();
  });
}

render();
