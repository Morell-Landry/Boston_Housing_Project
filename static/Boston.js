document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const inputs = document.querySelectorAll("input");
    const submitButton = document.querySelector("button");

    // Vérification dynamique des champs avec message d'erreur
    inputs.forEach(input => {
        input.addEventListener("input", function () {
            let errorMsg = this.nextElementSibling; // Sélectionne le message d'erreur

            if (this.value.trim() === "" || isNaN(this.value)) {
                this.classList.add("error-input");
                errorMsg.textContent = "Veuillez entrer une valeur numérique valide.";
                errorMsg.style.display = "block"; // Affiche l'erreur
            } else {
                this.classList.remove("error-input");
                this.classList.add("valid-input");
                errorMsg.textContent = ""; // Supprime l'erreur
            }
        });
    });

    // Animation au clic sur le bouton
    submitButton.addEventListener("click", function (event) {
        let isValid = true;
        inputs.forEach(input => {
            if (input.value.trim() === "" || isNaN(input.value)) {
                input.classList.add("error-input");
                input.nextElementSibling.textContent = "Ce champ est obligatoire !";
                input.nextElementSibling.style.display = "block";
                isValid = false;
            }
        });

        if (!isValid) {
            event.preventDefault(); // Bloque l'envoi si erreurs
        } else {
            submitButton.innerHTML = "⏳ Prédiction en cours...";
            submitButton.disabled = true;
            submitButton.classList.add("loading-button");
        }
    });
});
