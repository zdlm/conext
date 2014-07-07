define(['jquery','jquery.autosize','helper','text!../../html/publish.html'],function ($,autosize,helper,html) {
    function publish(element,url) {
        this.element = $(element);
        this.url = url;
        this.render();
        this._initEvents();
    }

    publish.prototype = {
        setModel: function (model) {
            this.model = model;
        },

        render: function () {
            this.element.html(html);
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

        _submit:function(){
            helper.api({
                url:this.url,
                type:"post",
                done:function(){
                    alert("success");
                }});
        },

        _initEvents:function(){
            $(".publish-content").bind("focus",this._toTyping);
            $(".publish-close").bind("click",this._close);
            $(".publish-content").bind("input",this._contentChange);
            $(".publish-content").bind("onpropertychange",this._contentChange);
            $(".publish-ok").bind("click",$.proxy( this, "_submit" ));
        }
    };

    return publish;
});
