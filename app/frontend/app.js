const form = document.getElementById("upload-form");
const output = document.getElementById("results");

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const fileInput = document.getElementById("code-file");
  const file = fileInput?.files?.[0];

  if (!file) {
    output.textContent = "Please select a file before analyzing.";
    return;
  }

  output.textContent = `Queued ${file.name} for backend analysis.`;
});
