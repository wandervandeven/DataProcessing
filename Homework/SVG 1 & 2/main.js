/* use this to test out your function */
window.onload = function() {
 	changeColor("fr", "#009900");
}


    
/* changeColor takes a path ID and a color (hex value)
   and changes that path's fill color */
function changeColor(id, color) {
    var change_Color = document.getElementById(id).style.fill = color;

}

