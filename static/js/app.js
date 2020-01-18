$(document).ready(() => {
    var ingredients = $(".ingredient").length;
    $("#add_ingredient").on("click", function () {
        $(".ingredient:first").clone().insertBefore("#add_ingredient").find("textarea").val("");
        ingredients += 1;
    });

    $("#remove_ingredient").on("click", function () {
        if (ingredients > 1) {
            /* only remove the :last item */
            $(this).siblings(".ingredient:last").remove();
            /* ensure original ingredient line never gets deleted */
            ingredients -= 1;
        }
    });

    var steps = $(".step").length;
    $("#add_step").on("click", function () {
        $(".step:first").clone().insertBefore("#add_step").find("textarea").val("");
        steps += 1;
    });

    $("#remove_step").on("click", function () {
        if (steps > 1) {
            /* only remove the :last item */
            $(this).siblings(".step:last").remove();
            /* ensure original ingredient line never gets deleted */
            steps -= 1;
        }
    });
});