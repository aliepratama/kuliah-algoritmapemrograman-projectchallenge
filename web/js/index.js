function validasi(){
    var email = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    if (email == '' || pass == ''){
        alert('Email atau Password harus diisi');
    }else{
        eel.auth(email, pass);
    }
}

function giveMsg(string){
    alert(string);
}

function dashboard(){
    window.location.href = 'pages/dashboard.html'
}

eel.expose(giveMsg);
eel.expose(dashboard);