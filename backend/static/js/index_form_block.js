/* -------------------- helpers -------------------- */
function showMessage(el, msg, asHTML = false) {
  if (asHTML) {
    el.innerHTML = msg;
  } else {
    el.textContent = msg;
  }
  el.classList.remove("hidden");
}

function hideMessage(el) {
  el.classList.add("hidden");
  el.textContent = "";
  el.innerHTML = ""; // clear both just in case
}

/* -------------------- main -------------------- */
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contact-form");
  const successMessage = document.getElementById("success-message");
  const errorMessage = document.getElementById("error-message");
  const submitBtn = form?.querySelector("button[type='submit']");

  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // UI: loading state
    submitBtn.disabled = true;
    submitBtn.classList.add("opacity-60", "cursor-not-allowed");

    // clear previous messages
    hideMessage(successMessage);
    hideMessage(errorMessage);

    const formData = new FormData(form);

    try {
      const res = await fetch("/api/v1/contact_form_submit", {
        method: "POST",
        body: formData,
      });

      // defensive JSON parse
      let data = {};
      try {
        data = await res.json();
      } catch {
        /* non-JSON response */
      }

      if (res.ok) {
        showMessage(
          successMessage,
          data.message || "Your submission was successful!",
          /* asHTML = */ true // <-- render tags
        );
        form.reset();
      } else {
        showMessage(
          errorMessage,
          data.message || "An error occurred. Please try again.",
          /* asHTML = */ false // plain text for errors
        );
      }
    } catch {
      showMessage(
        errorMessage,
        "A network error occurred. Please try again.",
        false
      );
    } finally {
      // restore button
      submitBtn.disabled = false;
      submitBtn.classList.remove("opacity-60", "cursor-not-allowed");

      // auto-hide success after 5 s
      if (!successMessage.classList.contains("hidden")) {
        setTimeout(() => hideMessage(successMessage), 5000);
      }
    }
  });
});
