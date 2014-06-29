define(['jquery','jquery.autosize','text!../../html/publish.html'],function ($,autosize,html) {
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
            this.element.html(html);
//            var self = this;
//            require(['text!../../html/publish.html'],function(html){
//                self.element.html(html);
//            });
        },

        _toTyping:function(){
            $(".publish-content").addClass("publish-content-active");
            $(".publish-operation").show();
            $(".publish-close").show();
        },

        _close:function(){
            $(".publish-content").removeClass("publish-content-active").val("").trigger('autosize.destroy');
            $(".publish-operation").hide();
            $(".publish-close").hide();
            $(".publish-ok").attr("disabled",true);
        },

        _contentChange:function(){
            var content = $(".publish-content");
            var button = $(".publish-ok");
            var value = content.val();
            if(value.length > 0){
                button.prop("disabled",false);
            }else{
                button.prop("disabled",true);
            }
            content.autosize();

        },

        _initEvents:function(){
            $(".publish-content").bind("focus",this._toTyping);
            $(".publish-close").bind("click",this._close);
            $(".publish-content").bind("input",this._contentChange);
            $(".publish-content").bind("onpropertychange",this._contentChange);
        }
    };

    return publish;
});
