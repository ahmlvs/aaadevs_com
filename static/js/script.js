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
