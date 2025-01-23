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


document.getElementById('formContact').addEventListener('submit', async (e) => {
    e.preventDefault();


    //Récupération des données du formulaire
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const sujet= document.getElementById('subject').value;
    const message = document.getElementById('message').value;

    try {
        //Transmet la requête au backend, et transform en JSON les formats voulu
        const reponse = await fetch('http://127.0.0.1:5000/contact', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
            },
            body: JSON.stringify({ name, email, phone, sujet, message}),
        });

        //Récupère les données obtenues par le backend
        const result = await response.json();

        if (reponse.ok) {
            alert(result.message);
        } else {
            alert(result.error);
        }
    } catch (error) {
        console.error('Erreur', error); 
        alert('Une erreur est survenue. Veuillez réessayer.')
    }
})