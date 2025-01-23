let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navLinks.forEach(links => {
                links.classList.remove('active');
            });
            document.querySelector('header nav a[href*="' + id + '"]').classList.add('active');
        }
    });
}

menuIcon.onclick = () => {
    console.log('Menu Icon clicked');
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
    console.log('Navbar active', navbar.classList.contains('active'));
}


const submitButton = document.getElementById('submit-btn')
const loader = document.getElementById('loader')

submitButton.addEventListener('click', async (e) => {
    e.preventDefault();

    //Afficher le loader et désactiver le bouton
    submitButton.disabled = true
    submitButton.value = '';
    loader.style.display = 'flex';

    //Récupération des données du formulaire
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const sujet = document.getElementById('subject').value;
    const message = document.getElementById('message').value;

    // Transmet la requête au backend, et transforme en JSON les formats voulus
    const response = await fetch('http://127.0.0.1:5000/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, phone, sujet, message }),
    });

    console.log(response);
    const result = await response.json();
    console.log(result);

    //Message d'erreur|succès de la requête
    if(response.ok) {
        alert('Message envoyé avec succès !', result.message);
    } else {
        alter('Erreur! Essayez à nouveau.');
    };

    //Reactivation du bouton
    setTimeout(() => {
       submitButton.disabled = false;
       loader.style.display = 'none';
       submitButton.value = 'Envoyé votre message'; 
    }, 3000);
})
