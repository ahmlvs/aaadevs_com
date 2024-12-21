// technology block
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

document.addEventListener("DOMContentLoaded", () => {
  const techItems = document.querySelectorAll(".image-container");

  techItems.forEach((item) => {
    const pixelCanvas = item.querySelector(".pixelCanvas");
    const ctx = pixelCanvas.getContext("2d", { willReadFrequently: true });
    const image = item.querySelector(".sourceImage");
    let isMouseOver = false;
    let animationFrameId;

    // Add click event listener with preventDefault
    item.addEventListener("click", (e) => {
      e.preventDefault();
    });

    // Load the image and draw it on the canvas
    image.onload = function () {
      ctx.drawImage(image, 0, 0, pixelCanvas.width, pixelCanvas.height);
      startPixelAnimation();
    };

    // Handle cached images
    if (image.complete) {
      image.onload();
    }

    // Start pixelation on hover
    item.addEventListener("mouseenter", () => {
      isMouseOver = true;
    });

    // Stop pixelation on hover out
    item.addEventListener("mouseleave", () => {
      isMouseOver = false;
    });

    function startPixelAnimation() {
      function updatePixels() {
        ctx.drawImage(image, 0, 0, pixelCanvas.width, pixelCanvas.height);
        const imageData = ctx.getImageData(
          0,
          0,
          pixelCanvas.width,
          pixelCanvas.height
        );
        const pixels = imageData.data;

        // Set the threshold based on whether the mouse is over the element
        const threshold = isMouseOver ? 0.95 : 1.0;

        for (let i = 0; i < pixels.length; i += 4) {
          if (Math.random() > threshold) {
            pixels[i + 3] = 0; // Set alpha to 0 (transparent)
          }
        }

        ctx.putImageData(imageData, 0, 0);
        animationFrameId = requestAnimationFrame(updatePixels);
      }

      updatePixels();
    }
  });
});
