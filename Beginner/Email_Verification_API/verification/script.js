document
	.getElementById("toggle-password")
	.addEventListener("click", function () {
		const passwordInput = document.getElementById("password");
		const type =
			passwordInput.getAttribute("type") === "password" ? "text" : "password";
		passwordInput.setAttribute("type", type);

		// Changer l'icône en fonction de l'état
		this.textContent = type === "password" ? "👁️" : "🚫";
	});
