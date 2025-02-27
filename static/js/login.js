(() => {
  const showPassword = document.getElementById("show_password");
  const passwordInput = document.getElementById("password_input");

  showPassword.addEventListener("click", () => {
    passwordInput.type =
      passwordInput.type === "password" ? "text" : "password";
    showPassword.textContent =
      passwordInput.type === "password" ? "Show" : "Hide";
  });
})();
