const form = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message");
const errorMessage = document.getElementById("error-message");

if (form) {
  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent page reload

    const formData = new FormData(form);
    const response = await fetch("/api/v1/contact_form_submit", {
      method: "POST",
      body: formData,
    });

    const data = await response.json(); // Parse JSON response

    if (response.ok) {
      // Show success message
      successMessage.style.display = "block";
      successMessage.innerHTML = data.message;
      form.reset(); // Clear the form
      errorMessage.style.display = "none"; // Hide error message
    } else {
      // Show error message
      errorMessage.style.display = "block";
      errorMessage.innerHTML = data.message;
      successMessage.style.display = "none"; // Hide success message
    }
  });
}
