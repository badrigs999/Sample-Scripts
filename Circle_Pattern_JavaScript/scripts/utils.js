
/*  Circles bound by a square  */
var inner_circle_dia, mid_point, outer_circle_dia, side_length;
side_length = 40;
mid_point = side_length / 2;
outer_circle_dia = mid_point - 2;
inner_circle_dia = outer_circle_dia - 3;

function drawCircle() {
    /*
    Iteratively walk through every point of the diagram and
    1. Calculate the distance to the center using the Pythagorean theorm.
    2. Draw a #, . depending on where the point lies.
    */
    var distance_to_center, drawing;
    drawing = "";

    for (var i = 0, _pj_a = side_length + 1; i < _pj_a; i += 1) {
        for (var j = 0, _pj_b = side_length + 1; j < _pj_b; j += 1) {
            distance_to_center = Math.sqrt(Math.pow(i - mid_point, 2) + Math.pow(j - mid_point, 2));

            if (distance_to_center <= inner_circle_dia) {
                drawing += "#";
            } 
            else {
                if (distance_to_center < outer_circle_dia) {
                    drawing += "0";
                } 
                else {
                    drawing += "#";
                }
            }
        }
        drawing += "</br>";
    }
    return drawing;
}
