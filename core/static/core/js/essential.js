document.addEventListener("DOMContentLoaded", ()=>{
    const requiredInputs = document.querySelectorAll("input[required]");

    requiredInputs.forEach(input =>{
        const label = document.querySelector(`label[for="${input.id}"]`);
        if(label){
            label.classList.add("required");
        }
    })
})