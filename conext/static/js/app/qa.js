require(["jquery","publish"], function ($,publish) {

    var publishTool = new publish("#qa-publish-container");

    var initEvents = function(){
        if(publishTool){
            $(publishTool).bind("submit",function(e,value){
               alert(value);
            });
        }
    };

    var init = function(){
        $("[data-value=qa]").addClass("active");
        initEvents();
    }();
});