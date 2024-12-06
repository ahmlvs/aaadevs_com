const form = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message");
const errorMessage = document.getElementById("error-message");

if (form) {
  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent page reload

    const formData = new FormData(form);

    try {
      const response = await fetch("/api/v1/contact_form_submit", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        successMessage.innerHTML =
          data.message || "Your submission was successful!";
        successMessage.classList.add("visible");
        errorMessage.classList.remove("visible");
      } else {
        const errorData = await response.json();
        errorMessage.innerHTML =
          errorData.message || "An error occurred. Please try again.";
        errorMessage.classList.add("visible");
        successMessage.classList.remove("visible");
      }
    } catch (error) {
      errorMessage.innerHTML = "A network error occurred. Please try again.";
      errorMessage.classList.add("visible");
      successMessage.classList.remove("visible");
    }

    // Hide messages after 5 seconds
    setTimeout(() => {
      successMessage.classList.remove("visible");
      errorMessage.classList.remove("visible");
    }, 5000);
  });
}

// Array of icon paths
const icons = [
  "/static/icons/javascript-programming-language-icon.webp",
  "/static/icons/mysql-icon.webp",
  "/static/icons/postgresql-icon.webp",
  "/static/icons/python-programming-language-icon.webp",
  "/static/icons/html-icon.webp",
];

// Function to generate sequential positions dynamically based on count
function generateSequentialPositions(count) {
  const positions = [];
  const step = 100 / count; // Divide the range 0-100 into equal parts

  for (let i = 0; i < count; i++) {
    const start = step * i; // Starting point of the range
    const end = start + step - 10; // End point of the range, keeping a buffer
    const position = Math.random() * (end - start) + start; // Random position within the range
    positions.push(position); // Push the calculated position
  }

  return positions;
}

// Function to add floating icons
function addFloatingIcons(container, icons, count = 4) {
  container.innerHTML = ""; // Clear existing icons

  // Generate sequential positions
  const positions = generateSequentialPositions(count);

  for (let i = 0; i < count; i++) {
    const icon = document.createElement("img");
    icon.src = icons[Math.floor(Math.random() * icons.length)]; // Randomly select an icon
    icon.alt = "Programming Icon";
    icon.className = "floating-icon";
    icon.style.left = `${positions[i]}%`; // Use calculated position
    icon.style.transform = `rotate(${Math.random() * 60}deg)`; // Random rotation
    container.appendChild(icon);
  }
}

// Target the floating-icons containers
const topIconsContainer = document.querySelector(".floating-icons-top");
const bottomIconsContainer = document.querySelector(".floating-icons-bottom");

// Add random icons to each container
if (topIconsContainer && bottomIconsContainer) {
  addFloatingIcons(topIconsContainer, icons, 4);
  addFloatingIcons(bottomIconsContainer, icons, 4);
}
