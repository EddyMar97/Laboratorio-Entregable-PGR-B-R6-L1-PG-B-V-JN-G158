function formuValid(){
    let RName = document.getElementById("RName").value;
    let RApellido = document.getElementById("RApellido").value;
    let REmail = document.getElementById("REmail").value;
    let Mensaje = document.getElementById("Mensaje").value;

    if (RName == "" || RApellido == "" || REmail == "" || Mensaje == ""){
        alert("Campo obligatorio");
        return false;
    } else {
        alert("Me pondré en contacto con usted prongo :)");
    }

    return true;
}