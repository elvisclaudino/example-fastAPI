document
  .getElementById("registerForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    let formData = new FormData(this);

    let response = await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      body: formData,
    });

    let result = await response.json();
    alert(result.message);
  });
