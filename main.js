const API = "http://localhost:8000";

document.getElementById("loadCards").addEventListener("click", async () => {
  const res = await fetch(`${API}/content/memories`);
  const items = await res.json();
  const grid = document.getElementById("cards");
  grid.innerHTML = items.map(cardHTML).join("");

  // Animate in
  requestAnimationFrame(() => {
    document.querySelectorAll(".card").forEach((el, i) => {
      setTimeout(() => el.classList.add("visible"), i * 120);
    });
  });
});

function cardHTML(item) {
  return `
    <article class="card rounded-lg bg-white shadow p-4">
      <img src="${item.image}" alt="${item.title}" class="rounded mb-3">
      <h4 class="font-semibold text-lg">${item.title}</h4>
      <p class="text-gray-700">${item.text}</p>
    </article>
  `;
}

document.getElementById("contactForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = new FormData(e.target);
  const payload = Object.fromEntries(form.entries());
  const status = document.getElementById("status");
  status.textContent = "Sending...";

  const res = await fetch(`${API}/contact/send`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  status.textContent = res.ok ? "Message sent!" : "Failed to send.";
});
