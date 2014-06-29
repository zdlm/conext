define(['jquery','jquery.autosize'],function ($,autosize) {
    function publish(element) {
        this.element = $(element);
        this.render();
        this._initEvents();
    }

    publish.prototype = {
        setModel: function (model) {
            this.model = model;
        },

        render: function () {
            var self = this;
            require(['text!../../html/publish.html'],function(html){
                self.element.html(html);
            });
        },

        _initEvents:function(){
             $(".publish-content").bind("focus",function(){
                 $(".publish-content").addClass("publish-content-active");
                 $(".publish-operation").show();
             });
        }
    };

    return publish;
});
