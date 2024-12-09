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

      let data;
      try {
        data = await response.json();
      } catch {
        data = {};
      }

      if (response.ok) {
        successMessage.innerHTML =
          data.message || "Your submission was successful!";
        successMessage.classList.add("visible");
        errorMessage.classList.remove("visible");
        form.reset();
      } else {
        errorMessage.innerHTML =
          data.message || "An error occurred. Please try again.";
        errorMessage.classList.add("visible");
        successMessage.classList.remove("visible");
      }
    } catch (error) {
      errorMessage.innerHTML = "A network error occurred. Please try again.";
      errorMessage.classList.add("visible");
      successMessage.classList.remove("visible");
    }

    // Hide success message after 5 seconds
    setTimeout(() => {
      successMessage.classList.remove("visible");
    }, 5000);
  });
}

const techItems = document.querySelectorAll(".tech-item[data-tech]");
const techName = document.getElementById("tech-name");
const techNameWrapper = document.getElementById("tech-name-wrapper");

// Function to reset the text and color
function resetTechName() {
  if (techName && techNameWrapper) {
    techName.textContent = "technology,";
    techNameWrapper.style.color = "";
  }
}

// Add event listeners to each technology item
if (techItems && techName && techNameWrapper) {
  techItems.forEach((item) => {
    item.addEventListener("mouseover", () => {
      const tech = item.getAttribute("data-tech");
      const color = item.getAttribute("data-color");

      techName.textContent = `${tech},`;
      techNameWrapper.style.color = color;
    });

    item.addEventListener("mouseout", resetTechName);
  });
}
