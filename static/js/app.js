$(document).ready(() => {
    var ingredientField = $(".ingredient").length;
    $("#add_ingredient").on("click", function () {
        // $("select").formSelect("destroy");
        $(".new-ingredient:first").clone().insertBefore("#add_ingredient").find("input[type='text'], select, textarea").val("");
        // $("select").formSelect();
        ingredientField += 1;
    });

    $("#remove_ingredient").on("click", function () {
        if (ingredientField > 1) {
            /* only remove the :last item */
            $(this).siblings(".new-ingredient:last").remove();
            /* ensure original ingredient line never gets deleted */
            ingredientField-= 1;
        }
    });

    var stepField = $(".step").length;
    $("#add_step").on("click", function () {
        // $("select").formSelect("destroy");
        $(".new-step:first").clone().insertBefore("#add_step").find("input[type='text'], select, textarea").val("");
        // $("select").formSelect();
        stepField += 1;
    });

    $("#remove_step").on("click", function () {
        if (stepField > 1) {
            /* only remove the :last item */
            $(this).siblings(".new-step:last").remove();
            /* ensure original ingredient line never gets deleted */
            stepField-= 1;
        }
    });
});