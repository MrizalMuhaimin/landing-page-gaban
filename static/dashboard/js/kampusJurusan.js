const domain2 = "http://127.0.0.1:8000"
//const domain2 = "https://gajahbanyuwangi.id"

const baseUrlKampus = domain2+"/api/kampus";
const baseUrlJurusan = domain2+"/api/jurusan";

const inputAlmamater =  document.getElementById("id_almamater_field")
const inputJurusan =  document.getElementById("id_jurusan_field")

document.getElementById("id_almamater_field").addEventListener("change", function(){
    getAllKampus()
    
})


const getAllKampus = async () => {
    try{

        const response = await fetch(`${baseUrlKampus}`);
        const responseJson = await response.json();
       
        if(responseJson.error) {
            showResponseMessage2(responseJson.message);
        } else {
            var id = getIDKampus(responseJson)
            getJurusanByIDKampus(id)

        }

    } catch(error) {
        // showResponseMessage(error)
        showResponseMessage2(error);
    }

}

const getJurusanByIDKampus = async(idKampus) =>{
    try{

        const response = await fetch(`${baseUrlJurusan}`);
        const responseJson = await response.json();
       
        if(responseJson.error) {
            showResponseMessage2(responseJson.message);
        } else {
            renderJurusan(idKampus,responseJson)

        }

    } catch(error) {
        // showResponseMessage(error)
        showResponseMessage2(error);
    }
}

function renderJurusan(idkampus, responseJson) {
    inputJurusan.innerText =""
    for (datajurusan of responseJson){
        if(datajurusan["kampus"]===idkampus){
            var x = document.createElement("OPTION");
            x.setAttribute("value", datajurusan["jurusan"]);
            x.innerText = datajurusan["jurusan"];
            inputJurusan.appendChild(x);
        }
    }
}

function getIDKampus(dataNamaKampus){
    for(datakampus of dataNamaKampus){
        if(datakampus.nama === document.getElementById("id_almamater_field").value ){
            return datakampus.id
        }
    }

}

const showResponseMessage2 = (message = "Check your internet connection") => {
    alert(message);

};
