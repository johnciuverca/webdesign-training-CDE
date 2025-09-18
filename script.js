// Get the button element
const button = document.getElementById("clickMe");

// Add a click event
button.addEventListener("click", () => {
  // Check if the image already exists
  if (!document.getElementById("showImage")) {
    const img = document.createElement("img");
    img.id = "showImage";
    img.src = "http://localhost:8000/nature.jpg"; // Fetch from local Python server
    img.alt = "Nature";
    img.style.display = "block";
    img.style.marginTop = "20px";
    button.insertAdjacentElement('afterend', img);
  }
});