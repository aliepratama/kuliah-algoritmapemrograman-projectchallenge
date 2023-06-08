let logoutButton = document.getElementById('logout');
logoutButton.addEventListener('click', ()=>{
    window.location.href = '../index.html';
});
arrayBulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
for(var i = 0;i < arrayBulan.length;i++){
    var optionBulan = document.createElement('option');
    optionBulan.value = i + 1;
    optionBulan.innerHTML = arrayBulan[i];
    document.getElementById('date_m').appendChild(optionBulan);
    var optionBulan = document.createElement('option');
    optionBulan.value = i + 1;
    optionBulan.innerHTML = arrayBulan[i];
    document.getElementById('fdate_m').appendChild(optionBulan);
}
setTimeout(()=>{
    var notTask = document.querySelectorAll('tr[toogle-done="false"]');
    var notTask_i3 = document.querySelectorAll('tr[toogle-done="false"]>td:nth-of-type(2)>i:nth-of-type(3)');
    var doneTask = document.querySelectorAll('tr[toogle-done="true"]');
    var doneTask_h = document.querySelectorAll('tr[toogle-done="true"]>td:nth-of-type(1)');
    var doneTask_i1 = document.querySelectorAll('tr[toogle-done="true"]>td:nth-of-type(2)>i:nth-of-type(1)');
    var doneTask_i2 = document.querySelectorAll('tr[toogle-done="true"]>td:nth-of-type(2)>i:nth-of-type(2)');
    var doneTask_i3 = document.querySelectorAll('tr[toogle-done="true"]>td:nth-of-type(2)>i:nth-of-type(3)');
    for(var i = 0;i < doneTask.length;i++){
        var content = doneTask_h[i].innerHTML;
        var strike = document.createElement('strike');
        strike.innerHTML = content;
        doneTask_h[i].innerHTML = '';
        doneTask_h[i].appendChild(strike);
        doneTask_i1[i].style.opacity = '0.5';
        doneTask_i1[i].style.cursor = 'default';
        doneTask_i2[i].style.opacity = '0.5';
        doneTask_i2[i].style.cursor = 'default';
        doneTask_i3[i].style.color = '#3A81E0';
        doneTask_i3[i].setAttribute('class', 'fa-solid fa-square-check');
        doneTask_i3[i].removeAttribute('id');
    }
    function iconHover(id){
        var ele = document.getElementById(id);
        ele.addEventListener('mouseover', ()=>{
            ele.style.opacity = '0.5';
            ele.setAttribute('class', 'fa-solid fa-square-check');
        });
        ele.addEventListener('mouseleave', ()=>{
            ele.style.opacity = '1';
            ele.setAttribute('class', 'fa-regular fa-square-check');
        });
    }
    for(var i = 0;i < notTask.length;i++){
        var ele = notTask_i3[i];
        ele.setAttribute('id', `notTask${i}`);
        iconHover(`notTask${i}`);
    }
}, 500);
async function isiAuto(){
    await eel.dateDisplay()(isiOtomatis);
}
modeSimpan = 'buat';
tokenTemp = '';
async function isiOtomatis(stringDate){
    modeSimpan = 'buat';
    stringDate = String(stringDate).split('-');
    document.getElementById('taskName').value = '';
    document.getElementById('date_d').value = stringDate[0];
    document.getElementById('date_m').value = stringDate[1];
    document.getElementById('date_y').value = stringDate[2];
}
function isiOtomatis2(token, namaTask, tanggal){
    modeSimpan = 'update';
    tokenTemp = token;
    tanggal = String(tanggal).split('-');
    document.getElementById('taskName').value = namaTask;
    document.getElementById('date_d').value = tanggal[0];
    document.getElementById('date_m').value = tanggal[1];
    document.getElementById('date_y').value = tanggal[2];
}
function task(){
    var name = document.getElementById('taskName').value;
    var day = document.getElementById('date_d').value;
    var month = document.getElementById('date_m').value;
    var year = document.getElementById('date_y').value;
    if(modeSimpan == 'buat'){
        eel.addTask(name, day, month, year);
    } else if (modeSimpan == 'update'){
        eel.updateTask(tokenTemp, name, day, month, year);
    } else{}
}
function sendNotif(obj){
    var data = obj;
    var tabel = document.getElementById('tableListTask');
    for(var i = 0;i < data.length;i++){
        var ele = document.createElement('tr');
        ele.setAttribute('toogle-done', data[i][4]);
        if(data[i][4] == 'true'){
            ele.innerHTML = `<td>${data[i][1]}</td>
            <td class="d-flex py-3 justify-content-center align-items-center">
                <i class="fa-solid fa-trash me-3" onclick="eel.deleteTask('${data[i][0]}')"></i>
                <i class="fa-solid fa-pen-to-square me-3" data-bs-toggle="modal" data-bs-target="#tambahTaskModal" onclick="isiOtomatis2('${data[i][0]}','${data[i][1]}','${data[i][2]}')"></i>
                <i class="fa-regular fa-square-check" onclick="eel.changeStatusTask('${data[i][0]}', 'false')"></i>
            </td>`;
        } else {
            ele.innerHTML = `<td>${data[i][1]}</td>
            <td class="d-flex py-3 justify-content-center align-items-center">
                <i class="fa-solid fa-trash me-3" onclick="eel.deleteTask('${data[i][0]}')"></i>
                <i class="fa-solid fa-pen-to-square me-3" data-bs-toggle="modal" data-bs-target="#tambahTaskModal" onclick="isiOtomatis2('${data[i][0]}','${data[i][1]}','${data[i][2]}')"></i>
                <i class="fa-regular fa-square-check" onclick="eel.changeStatusTask('${data[i][0]}', 'true')"></i>
            </td>`;
        }
        tabel.appendChild(ele);
    }
}
function reload() {
    window.location.reload();
}
function giveAlert(string) {
    window.alert(string)
}
eel.everyReload();
eel.expose(sendNotif);
eel.expose(reload);
eel.expose(giveAlert);
