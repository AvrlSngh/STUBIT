
window.onload = function() {

}


// for dropdown
function display_toggle() {
  document.getElementById('tools_list').classList.toggle('show');
}

window.onclick = function(e) {
  if(!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById('tools_list');
    if(myDropdown.classList.contains('show')){
      myDropdown.classList.remove('show');
    }
  }
}


window.onload = function() {
// adding functionalities to the mynotes models
// Get the modal
if(window.location.pathname == /students/)
{
var modal = document.getElementById('mynotesID');

// Get the button that opens the modal
var btn = document.getElementById("addMynote");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "flex";
    modal.style.justifyContent = "center";
    modal.style.alignItems = "center";

}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
document.getElementById("id_body").cols = 0;

// slugifying the title
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g, '-')
};

titleInput.addEventListener('keyup', (e)=>{
  slugInput.setAttribute('value', slugify(titleInput.value));
});
}

else {
  // for validating filter field

  document.getElementById('id_semester').onclick = function() {validate_filter()};


  function validate_filter() {
  var semester = document.getElementById('id_semester').value;

  if(semester == 1 || semester == 2)
  {
    document.getElementById('id_branch').disabled =  true;
  }

  else if (semester != 1 || semester != 2) {
    document.getElementById('id_branch').disabled =  false;
  }
  }
}

}
