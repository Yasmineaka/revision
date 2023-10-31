// menu burger 

document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger-menu');
    const mobileMenu = document.querySelector('.menu-mobile');

    // Gestion du clic sur le menu hamburger
    hamburger.addEventListener('click', function () {
        mobileMenu.classList.toggle('active');
    });
});







// JavaScript pour la validation du formulaire de contact
const contactForm = document.getElementById('contact-form');
const successPopup = document.getElementById('success-popup');

contactForm.addEventListener('submit', function (e) {
    e.preventDefault();

    // Récupérer les valeurs des champs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Validation simple (vérifiez si les champs ne sont pas vides)
    if (name.trim() === '' || email.trim() === '' || message.trim() === '') {
        alert('Veuillez remplir tous les champs du formulaire.');
    } else {
        // Afficher la popup de confirmation
        $(successPopup).modal('show');
        contactForm.reset(); // Réinitialise le formulaire
    }
});





// education et experience


function showcompetences(category) {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => button.classList.remove('active'));
    document.querySelector(`.btn.${category}-btn`).classList.add('active');

    // Cacher le contenu actif
    const activeContent = document.querySelector('.active-content');
    if (activeContent) {
        activeContent.style.display = 'none';
        activeContent.classList.remove('active-content');
    }

    // Afficher le contenu correspondant
    const contentToShow = document.querySelector(`.${category}-content`);
    if (contentToShow) {
        contentToShow.style.display = 'block';
        contentToShow.classList.add('active-content');
    }
}

// Afficher les compétences "Expérience" par défaut
showcompetences('experience');




// bouton pour revenir en haut


// Sélectionnez le bouton et attachez un gestionnaire d'événements au défilement
const backToTopButton = document.getElementById('bouton_retour');
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        // Affichez le bouton lorsque vous avez fait défiler suffisamment vers le bas
        backToTopButton.style.display = 'block';
    } else {
        // Masquez le bouton lorsque vous êtes en haut de la page
        backToTopButton.style.display = 'none';
    }
});

// Ajoutez un gestionnaire d'événements pour le clic sur le bouton
backToTopButton.addEventListener('click', () => {
    window.scrollTo(0, 0); // Faites défiler la page en haut
});
