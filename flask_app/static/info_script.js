// time to do shit again

let classInfo = document.getElementById('raceinfo');
// async function for api request from approute in controller file
async function getClass(){
    const response = await (await fetch('/api/show/info')).json();
    // object returning from the api
    const infoList = response;
    console.log(response)
    classInfo.innerHTML += 
    `
    <div class='card text-wrap mt-2 p-3'>
    <h1>${infoList.name}</h1>
    <h2>Speed: ${infoList.speed}</h2>
    <p class='fs-4 fw-bolder'>Alignment: ${infoList.alignment}</p>
    <p class='fs-4 fw-bolder'>Age: ${infoList.age}</p>
    <p class='fs-4 fw-bolder'>Size: ${infoList.size}</p>
    <p class='fs-4 fw-bolder'>Size Description: ${infoList.size_description}</p>
    </div>
    `
}
getClass()


