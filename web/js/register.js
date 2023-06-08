function create(){
    var email = document.getElementById('email').value;
    var nama = document.getElementById('name').value;
    var password1 = document.getElementById('pass').value;
    var password2 = document.getElementById('pass2').value;

    if (password1 != password2){
        alert('Password tidak cocok')
    } else {
        eel.createAkun(email, nama, password1)
        
    }

}
function giveMsg(string){
    alert(string);
}

function dashboard(){
    window.location.href = 'dashboard.html'
}
eel.expose(giveMsg);
eel.expose(dashboard);