// Smooth scroll for nav links
document.querySelectorAll("a[href^='#']").forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
});

// Simple search filter (for blog listing page)
function filterPosts() {
  let input = document.getElementById("search").value.toLowerCase();
  let cards = document.getElementsByClassName("card");
  
  Array.from(cards).forEach(card => {
    let title = card.querySelector("h3").innerText.toLowerCase();
    card.style.display = title.includes(input) ? "block" : "none";
  });
}
