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

//function séparer pour la Validation de l'émail
function valideEmail() {
    const email = document.getElementById('email').value;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const Errormail = document.getElementById('Errormail');
    submitButton.disabled = true
    submitButton.value = '';
    loader.style.display = 'flex';
    

    //Validation de l'émail
    if(!emailRegex.test(email)) {
        Errormail.textContent ='Veuillez entrer une adresse mail valide.';
        return false;
    } else {
        Errormail.textContent='';
        return true;
    }
}

//function séparer pour la Validation du numéro de téléphone
function valideTel() {
    const phone = document.getElementById('phone').value;
    const phoneRegex = /^(\+33|0)[1-9](\d{2}){4}$/;
    const Errorphone = document.getElementById('Errorphone');

    if(!phoneRegex.test(phone)) {
        Errorphone.textContent = 'Veuillez entrer un numéro de téléphone valide.';
        return false;
    } else {
        Errorphone.textContent = '';
        return true;
    };

}


//function séparer pour gérer le message
function valideMessage() {
    const message = document.getElementById('message').value;
    const Errormessage = document.getElementById('Errormessage');

    if (message.length > 20) {
        Errormessage.textContent = 'Votre message ne doit pas dépasser 200 caractères.';
        return false;
    } else {
        Errormessage.textContent = '';
        return true;
    };
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

    //Vérification des entrées du formulaire
    let isValid = true;

        if(!valideEmail()) {
            isValid = false;
        }

        if(!valideTel()) {
            isValid = false;
        }

        if(!valideMessage()) {
            isValid = false;
        }

        if (isValid) {
            try {
            // Transmet la requête au backend, et transforme en JSON les formats voulus
            const response = await fetch('https://portfolio-project-55u9.onrender.com/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, phone, sujet, message }),
            });

            //Affichage du résultat du statu et le contenu si ce n'est pas JSON
            if(!response.ok) {
                const errorText = await response.text();
                throw new Error('Erreur ${response.status} : ${errorText}');
            }

            console.log(response);
            const result = await response.json()
            console.log(result);

            //Message d'erreur|succès de la requête
            if(response.ok) {
                alert('Message envoyé avec succès !');
                document.getElementById('formContact').reset();
            } else {
                alert('Erreur! Essayez à nouveau.');
            }
        } catch (error) {
            console.error('Erreur lors de l\'envois du formulaire : ' + error);
            alert('Une erreur est survenue. Veuillez réessayer.');
        } 
    }
    
    //Reactivation du bouton
    setTimeout(() => {
    submitButton.disabled = false;
    loader.style.display = 'none';
    submitButton.value = 'Envoyé votre message'; 
    }, 3000);
    })